"""
Main Module for Manufacturer Finder Tool
Orchestrates the complete workflow
"""

import os
import sys
import logging
import argparse
from pathlib import Path
from data_loader import DataLoader
from manufacturer_finder import ManufacturerFinder
from excel_exporter import ExcelExporter

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('manufacturer_finder.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ManufacturerFinderApp:
    """Main application orchestrator"""
    
    def __init__(self, excel_path: str, api_key: str = None, output_path: str = None):
        """
        Initialize the application
        
        Args:
            excel_path (str): Path to input Excel file
            api_key (str, optional): OpenAI API key
            output_path (str, optional): Output Excel file path
        """
        self.excel_path = excel_path
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.output_path = output_path
        
        # Validate inputs
        if not os.path.exists(excel_path):
            raise FileNotFoundError(f"Excel file not found: {excel_path}")
        
        if not self.api_key:
            raise ValueError("OpenAI API key required. Set OPENAI_API_KEY environment variable or provide via --api-key")
        
        logger.info(f"Initialized ManufacturerFinderApp with input: {excel_path}")
    
    def run(self, max_manufacturers: int = 5) -> str:
        """
        Run the complete manufacturer analysis workflow
        
        Args:
            max_manufacturers (int): Maximum manufacturers to find per item
            
        Returns:
            str: Path to output Excel file
        """
        try:
            logger.info("="*80)
            logger.info("STARTING MANUFACTURER FINDER ANALYSIS")
            logger.info("="*80)
            
            # Step 1: Load data
            logger.info("\n[STEP 1/3] Loading Excel data...")
            loader = DataLoader(self.excel_path)
            df = loader.load_excel()
            
            if not loader.validate_data(df):
                raise ValueError("Data validation failed. Check Excel file format.")
            
            logger.info(f"✓ Loaded {len(df)} items from Excel")
            
            # Step 2: Find manufacturers
            logger.info("\n[STEP 2/3] Finding credible manufacturers using OpenAI...")
            finder = ManufacturerFinder(api_key=self.api_key)
            results_df = finder.find_manufacturers(df, max_manufacturers=max_manufacturers)
            
            logger.info(f"✓ Analyzed {len(results_df)} items")
            
            # Step 3: Export results
            logger.info("\n[STEP 3/3] Exporting results to Excel...")
            exporter = ExcelExporter(output_path=self.output_path)
            output_file = exporter.create_summary_sheet(results_df)
            
            logger.info(f"✓ Results exported to: {output_file}")
            
            # Print summary
            self._print_summary(results_df, output_file)
            
            logger.info("\n" + "="*80)
            logger.info("ANALYSIS COMPLETED SUCCESSFULLY")
            logger.info("="*80)
            
            return output_file
            
        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}", exc_info=True)
            raise
    
    def _print_summary(self, df, output_file):
        """Print analysis summary"""
        logger.info("\n" + "="*80)
        logger.info("ANALYSIS SUMMARY")
        logger.info("="*80)
        logger.info(f"Total items analyzed: {len(df)}")
        
        if 'Avg_Credibility_Score' in df.columns:
            avg_score = df['Avg_Credibility_Score'].mean()
            logger.info(f"Average credibility score: {avg_score:.2f}")
            
            high_credibility = len(df[df['Avg_Credibility_Score'] >= 80])
            medium_credibility = len(df[(df['Avg_Credibility_Score'] >= 60) & (df['Avg_Credibility_Score'] < 80)])
            low_credibility = len(df[df['Avg_Credibility_Score'] < 60])
            
            logger.info(f"High credibility (≥80): {high_credibility} items")
            logger.info(f"Medium credibility (60-79): {medium_credibility} items")
            logger.info(f"Low credibility (<60): {low_credibility} items")
        
        logger.info(f"\nResults saved to: {output_file}")


def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(
        description='Find credible manufacturers using OpenAI API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with environment variable for API key
  python main.py input.xlsx
  
  # Specify API key and output file
  python main.py input.xlsx --api-key sk-xxx --output results.xlsx
  
  # Limit number of manufacturers per item
  python main.py input.xlsx --max-manufacturers 3
        """
    )
    
    parser.add_argument(
        'excel_file',
        help='Path to input Excel file with MPN, Model Description, and Quantity'
    )
    
    parser.add_argument(
        '--api-key',
        help='OpenAI API key (or set OPENAI_API_KEY environment variable)',
        default=None
    )
    
    parser.add_argument(
        '--output',
        help='Output Excel file path (auto-generated if not provided)',
        default=None
    )
    
    parser.add_argument(
        '--max-manufacturers',
        type=int,
        default=5,
        help='Maximum number of manufacturers to find per item (default: 5)'
    )
    
    args = parser.parse_args()
    
    try:
        app = ManufacturerFinderApp(
            excel_path=args.excel_file,
            api_key=args.api_key,
            output_path=args.output
        )
        
        output_file = app.run(max_manufacturers=args.max_manufacturers)
        
        print(f"\n✓ Success! Results saved to: {output_file}")
        sys.exit(0)
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        print(f"\n✗ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

