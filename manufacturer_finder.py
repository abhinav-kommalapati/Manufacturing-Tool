"""
Manufacturer Finder Module
Uses OpenAI API to find credible manufacturers based on MPN and model description
"""

import os
import logging
import pandas as pd
from typing import List, Dict, Optional
from openai import OpenAI
import json
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ManufacturerFinder:
    """Finds credible manufacturers using OpenAI API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize ManufacturerFinder with OpenAI API key
        
        Args:
            api_key (str, optional): OpenAI API key. If not provided, reads from environment
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        
        if not self.api_key:
            raise ValueError("OpenAI API key not provided. Set OPENAI_API_KEY environment variable or pass api_key parameter")
        
        self.client = OpenAI(api_key=self.api_key)
        logger.info("ManufacturerFinder initialized with OpenAI API")
    
    def find_manufacturers(self, df: pd.DataFrame, max_manufacturers: int = 5) -> pd.DataFrame:
        """
        Find manufacturers for each item in the DataFrame
        
        Args:
            df (pd.DataFrame): DataFrame with MPN, Model_Description, Quantity
            max_manufacturers (int): Maximum number of manufacturers to find per item
            
        Returns:
            pd.DataFrame: Enhanced DataFrame with manufacturer information
        """
        results = []
        
        for idx, row in df.iterrows():
            logger.info(f"Processing row {idx + 1}/{len(df)}: {row['MPN']}")
            
            try:
                manufacturer_info = self._query_manufacturers(
                    mpn=row['MPN'],
                    description=row['Model_Description'],
                    quantity=row['Quantity'],
                    max_results=max_manufacturers
                )
                
                # Add manufacturer info to row
                result_row = row.to_dict()
                result_row.update(manufacturer_info)
                results.append(result_row)
                
                # Rate limiting - avoid hitting API too fast
                time.sleep(0.5)
                
            except Exception as e:
                logger.error(f"Error processing row {idx}: {str(e)}")
                result_row = row.to_dict()
                result_row.update({
                    'Manufacturers': 'Error',
                    'Credibility_Score': 0,
                    'Recommendation': f'Error: {str(e)}',
                    'Details': ''
                })
                results.append(result_row)
        
        return pd.DataFrame(results)
    
    def _query_manufacturers(self, mpn: str, description: str, quantity: int, max_results: int = 5) -> Dict:
        """
        Query OpenAI to find credible manufacturers
        
        Args:
            mpn (str): Manufacturing Part Number
            description (str): Model/product description
            quantity (int): Quantity needed
            max_results (int): Maximum manufacturers to return
            
        Returns:
            Dict: Manufacturer information
        """
        prompt = f"""Given the following manufacturing part information, identify the most credible manufacturers:

Manufacturing Part Number (MPN): {mpn}
Model/Product Description: {description}
Quantity Required: {quantity}

Please provide:
1. Top {max_results} credible manufacturers for this part
2. A credibility score (0-100) for each manufacturer based on:
   - Industry reputation
   - Product quality
   - Supply chain reliability
   - Market presence
3. Brief reasoning for your recommendation
4. Any important considerations (minimum order quantities, lead times, certifications)

Format your response as a JSON object with the following structure:
{{
    "manufacturers": [
        {{
            "name": "Manufacturer Name",
            "credibility_score": 95,
            "strengths": ["strength1", "strength2"],
            "considerations": "Any important notes"
        }}
    ],
    "overall_recommendation": "Your top recommendation and why",
    "additional_info": "Any other relevant information"
}}
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in manufacturing and supply chain management. You have deep knowledge of credible manufacturers across various industries, their reputations, and product quality. Provide accurate, detailed recommendations based on industry standards."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1500,
                response_format={"type": "json_object"}
            )
            
            # Parse the response
            result = json.loads(response.choices[0].message.content)
            
            # Extract and format manufacturer information
            manufacturers = result.get('manufacturers', [])
            
            # Create formatted output
            manufacturer_names = [m.get('name', 'Unknown') for m in manufacturers]
            credibility_scores = [m.get('credibility_score', 0) for m in manufacturers]
            
            # Calculate average credibility
            avg_credibility = sum(credibility_scores) / len(credibility_scores) if credibility_scores else 0
            
            # Format detailed information
            details = []
            for m in manufacturers:
                name = m.get('name', 'Unknown')
                score = m.get('credibility_score', 0)
                strengths = ', '.join(m.get('strengths', []))
                considerations = m.get('considerations', '')
                details.append(f"{name} (Score: {score})\nStrengths: {strengths}\nNotes: {considerations}")
            
            return {
                'Top_Manufacturer': manufacturer_names[0] if manufacturer_names else 'Not Found',
                'All_Manufacturers': ' | '.join(manufacturer_names),
                'Avg_Credibility_Score': round(avg_credibility, 2),
                'Recommendation': result.get('overall_recommendation', 'No recommendation available'),
                'Detailed_Analysis': '\n\n'.join(details),
                'Additional_Info': result.get('additional_info', '')
            }
            
        except Exception as e:
            logger.error(f"Error querying OpenAI: {str(e)}")
            raise
    
    def analyze_single_part(self, mpn: str, description: str, quantity: int = 1) -> Dict:
        """
        Analyze a single part and return manufacturer recommendations
        
        Args:
            mpn (str): Manufacturing Part Number
            description (str): Model/product description
            quantity (int): Quantity needed
            
        Returns:
            Dict: Manufacturer analysis
        """
        return self._query_manufacturers(mpn, description, quantity)
