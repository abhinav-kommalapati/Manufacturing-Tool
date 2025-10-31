"""
Data Loader Module
Handles reading Excel files with Oracle MPN, Model Description, and Quantity
"""

import pandas as pd
import logging
from typing import List, Dict, Optional

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    """Handles loading Excel data with manufacturing part information"""
    
    def __init__(self, file_path: str):
        """
        Initialize DataLoader with file path
        
        Args:
            file_path (str): Path to the Excel file
        """
        self.file_path = file_path
        
    def load_excel(self) -> pd.DataFrame:
        """
        Load Excel file and extract MPN, model description, and quantity
        
        Returns:
            pd.DataFrame: DataFrame with manufacturing part information
        """
        try:
            logger.info(f"Loading Excel file: {self.file_path}")
            
            # Read the Excel file
            df = pd.read_excel(self.file_path)
            
            logger.info(f"Loaded Excel with {len(df)} rows and {len(df.columns)} columns")
            logger.info(f"Columns found: {list(df.columns)}")
            
            # Clean and standardize the data
            cleaned_df = self._clean_data(df)
            
            logger.info(f"Cleaned data: {len(cleaned_df)} valid rows")
            return cleaned_df
            
        except Exception as e:
            logger.error(f"Error loading Excel file: {str(e)}")
            raise
    
    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and standardize the DataFrame
        
        Args:
            df (pd.DataFrame): Original DataFrame
            
        Returns:
            pd.DataFrame: Cleaned DataFrame
        """
        # Try to identify columns automatically
        df_clean = df.copy()
        
        # Standardize column names (case-insensitive matching)
        column_mapping = {}
        for col in df.columns:
            col_lower = str(col).lower().strip()
            if any(x in col_lower for x in ['mpn', 'part number', 'part_number', 'partnumber']):
                column_mapping[col] = 'MPN'
            elif any(x in col_lower for x in ['model', 'description', 'product']):
                column_mapping[col] = 'Model_Description'
            elif any(x in col_lower for x in ['quantity', 'qty', 'amount']):
                column_mapping[col] = 'Quantity'
        
        # Rename columns if mapping found
        if column_mapping:
            df_clean = df_clean.rename(columns=column_mapping)
            logger.info(f"Mapped columns: {column_mapping}")
        
        # Ensure required columns exist
        required_cols = ['MPN', 'Model_Description', 'Quantity']
        missing_cols = [col for col in required_cols if col not in df_clean.columns]
        
        if missing_cols:
            logger.warning(f"Missing columns: {missing_cols}")
            # Use first three columns as fallback
            if len(df_clean.columns) >= 3:
                logger.info("Using first 3 columns as MPN, Model_Description, Quantity")
                df_clean.columns = required_cols + list(df_clean.columns[3:])
        
        # Remove rows with missing critical data
        df_clean = df_clean.dropna(subset=['MPN', 'Model_Description'])
        
        # Fill missing quantities with 1
        if 'Quantity' in df_clean.columns:
            df_clean['Quantity'] = df_clean['Quantity'].fillna(1)
        else:
            df_clean['Quantity'] = 1
        
        # Convert quantity to integer
        df_clean['Quantity'] = pd.to_numeric(df_clean['Quantity'], errors='coerce').fillna(1).astype(int)
        
        # Add ID column
        df_clean.insert(0, 'ID', range(1, len(df_clean) + 1))
        
        return df_clean
    
    def validate_data(self, df: pd.DataFrame) -> bool:
        """
        Validate that the DataFrame has required columns
        
        Args:
            df (pd.DataFrame): DataFrame to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        required_columns = ['MPN', 'Model_Description', 'Quantity']
        
        for col in required_columns:
            if col not in df.columns:
                logger.error(f"Missing required column: {col}")
                return False
        
        if len(df) == 0:
            logger.error("DataFrame is empty")
            return False
        
        return True

