"""
Example Usage Script
Demonstrates how to use the Manufacturer Finder Tool programmatically
"""

import os
from data_loader import DataLoader
from manufacturer_finder import ManufacturerFinder
from excel_exporter import ExcelExporter

def example_single_part_analysis():
    """Example: Analyze a single part"""
    print("="*60)
    print("Example 1: Single Part Analysis")
    print("="*60)
    
    # Set your API key (or use environment variable)
    api_key = os.getenv('OPENAI_API_KEY', 'your-api-key-here')
    
    # Initialize finder
    finder = ManufacturerFinder(api_key=api_key)
    
    # Analyze a single part
    result = finder.analyze_single_part(
        mpn="ABC-12345",
        description="Industrial servo motor 5HP with encoder",
        quantity=100
    )
    
    print("\nResults:")
    print(f"Top Manufacturer: {result['Top_Manufacturer']}")
    print(f"Credibility Score: {result['Avg_Credibility_Score']}")
    print(f"Recommendation: {result['Recommendation']}")
    print("\n" + "="*60)


def example_batch_analysis():
    """Example: Analyze multiple parts from Excel"""
    print("="*60)
    print("Example 2: Batch Analysis from Excel")
    print("="*60)
    
    # Set your API key
    api_key = os.getenv('OPENAI_API_KEY', 'your-api-key-here')
    
    # Load data from Excel
    print("\nLoading data from example_input.xlsx...")
    loader = DataLoader('example_input.xlsx')
    df = loader.load_excel()
    
    print(f"Loaded {len(df)} items")
    print("\nData preview:")
    print(df.head())
    
    # Find manufacturers
    print("\nFinding manufacturers (this may take a few minutes)...")
    finder = ManufacturerFinder(api_key=api_key)
    results_df = finder.find_manufacturers(df, max_manufacturers=3)
    
    print("\nAnalysis complete!")
    print(f"\nResults preview:")
    print(results_df[['MPN', 'Top_Manufacturer', 'Avg_Credibility_Score']].head())
    
    # Export results
    print("\nExporting to Excel...")
    exporter = ExcelExporter(output_path='example_results.xlsx')
    output_file = exporter.create_summary_sheet(results_df)
    
    print(f"✓ Results saved to: {output_file}")
    print("\n" + "="*60)


def example_custom_configuration():
    """Example: Custom configuration and settings"""
    print("="*60)
    print("Example 3: Custom Configuration")
    print("="*60)
    
    # Initialize with custom settings
    api_key = os.getenv('OPENAI_API_KEY', 'your-api-key-here')
    finder = ManufacturerFinder(api_key=api_key)
    
    # Analyze with specific requirements
    result = finder.analyze_single_part(
        mpn="XYZ-67890",
        description="Precision ball bearing assembly for high-speed applications",
        quantity=500  # Large quantity
    )
    
    print("\nFor high-volume orders:")
    print(f"Manufacturers: {result['All_Manufacturers']}")
    print(f"Additional Info: {result['Additional_Info']}")
    print("\n" + "="*60)


if __name__ == "__main__":
    print("\n")
    print("="*60)
    print(" MANUFACTURER FINDER - USAGE EXAMPLES")
    print("="*60)
    print("\nMake sure to set your OPENAI_API_KEY before running!")
    print("\nChoose an example to run:\n")
    print("1. Single Part Analysis")
    print("2. Batch Analysis from Excel (recommended)")
    print("3. Custom Configuration")
    print("4. Run all examples")
    print("\n")
    
    choice = input("Enter choice (1-4) or press Enter to skip: ").strip()
    
    if not choice:
        print("\nTo run examples, use:")
        print("  python example_usage.py")
        print("\nOr use the web interface:")
        print("  streamlit run app.py")
    else:
        if choice in ['1', '4']:
            example_single_part_analysis()
            print("\n")
        
        if choice in ['2', '4']:
            example_batch_analysis()
            print("\n")
        
        if choice in ['3', '4']:
            example_custom_configuration()
            print("\n")
        
        print("✓ Examples completed!")
        print("\nNext steps:")
        print("- Prepare your own Excel file")
        print("- Run: streamlit run app.py")
        print("- Or: python main.py your_data.xlsx")
