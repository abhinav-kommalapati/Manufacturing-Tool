# 🏭 Manufacturer Finder Tool

An AI-powered tool to find credible manufacturers based on Manufacturing Part Numbers (MPN), model descriptions, and quantity requirements using OpenAI's GPT-4.

## 📋 Overview

This tool analyzes your manufacturing parts data and provides:
- **Top manufacturer recommendations** for each part
- **Credibility scores** (0-100) based on industry reputation, quality, and reliability
- **Detailed analysis** including strengths and considerations
- **Formatted Excel reports** with visual credibility indicators

## ✨ Features

- 🤖 **AI-Powered Analysis**: Uses OpenAI GPT-4 for intelligent manufacturer recommendations
- 📊 **Excel Integration**: Reads Excel input and exports formatted results
- 🎨 **Beautiful Web Interface**: Streamlit-based UI for easy interaction
- 📈 **Credibility Scoring**: Rates manufacturers on a 0-100 scale
- 📁 **Batch Processing**: Analyze multiple parts at once
- 📝 **Detailed Reports**: Get comprehensive analysis for each part

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone or navigate to the project directory:**
```bash
cd "/Users/abhinav/Desktop/DynaPrice Internship/Manufacturing tool"
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up your OpenAI API key:**

**Option A: Environment Variable (Recommended)**
```bash
export OPENAI_API_KEY='your-api-key-here'
```

**Option B: .env File**
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your-api-key-here
```

**Option C: Provide via Command Line or UI**
You can also provide the API key when running the tool.

## 📖 Usage

### Method 1: Web Interface (Recommended)

Launch the Streamlit web application:

```bash
streamlit run app.py
```

Then:
1. Open your browser to the displayed URL (usually http://localhost:8501)
2. Enter your OpenAI API key in the sidebar (if not set as environment variable)
3. Upload your Excel file
4. Click "Start Analysis"
5. Download the results

### Method 2: Command Line

```bash
python main.py your_data.xlsx
```

**Advanced Options:**

```bash
# Specify API key
python main.py your_data.xlsx --api-key sk-your-key-here

# Custom output file
python main.py your_data.xlsx --output results.xlsx

# Limit manufacturers per item
python main.py your_data.xlsx --max-manufacturers 3

# All options combined
python main.py input.xlsx --api-key sk-xxx --output results.xlsx --max-manufacturers 5
```

## 📊 Excel File Format

Your input Excel file should contain these columns (column names are auto-detected):

| Column | Description | Example |
|--------|-------------|---------|
| **MPN** | Manufacturing Part Number | ABC-12345 |
| **Model Description** | Product/model description | Industrial servo motor 5HP |
| **Quantity** | Quantity needed | 100 |

**Supported column name variations:**
- MPN: `MPN`, `Part Number`, `PartNumber`, `Part_Number`
- Description: `Model`, `Description`, `Product`, `Model Description`
- Quantity: `Quantity`, `Qty`, `Amount`

### Example Input

```
| MPN        | Model Description              | Quantity |
|------------|-------------------------------|----------|
| ABC-12345  | Industrial servo motor 5HP    | 100      |
| XYZ-67890  | Precision bearing assembly    | 250      |
| DEF-11111  | Control panel with HMI        | 50       |
```

## 📤 Output

The tool generates an Excel file with two sheets:

### 1. **Summary Sheet**
- ID
- MPN
- Model Description
- Top Manufacturer
- Average Credibility Score (color-coded)

### 2. **Detailed Analysis Sheet**
- All input columns
- Top Manufacturer
- All Manufacturers (list)
- Average Credibility Score (color-coded)
- Recommendation
- Detailed Analysis (strengths, considerations for each manufacturer)
- Additional Information

**Credibility Score Color Coding:**
- 🟢 Green (≥80): High credibility
- 🟡 Yellow (60-79): Medium credibility
- 🔴 Red (<60): Low credibility, needs review

## 🔍 How It Works

1. **Data Loading**: Reads your Excel file and validates the data
2. **AI Analysis**: For each part, queries OpenAI GPT-4 with:
   - Manufacturing Part Number (MPN)
   - Model/Product Description
   - Quantity Required
3. **Manufacturer Research**: AI analyzes:
   - Industry reputation
   - Product quality
   - Supply chain reliability
   - Market presence
   - Certifications and standards
4. **Scoring**: Assigns credibility scores (0-100) to each manufacturer
5. **Export**: Generates formatted Excel report with visual indicators

## 📁 Project Structure

```
Manufacturing tool/
├── app.py                    # Streamlit web application
├── main.py                   # Command-line interface
├── data_loader.py            # Excel data loading and validation
├── manufacturer_finder.py    # OpenAI integration and analysis
├── excel_exporter.py         # Excel export with formatting
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── manufacturer_finder.log   # Application logs
```

## 🛠️ Modules

### `data_loader.py`
- Loads Excel files
- Auto-detects columns
- Validates data
- Cleans and standardizes input

### `manufacturer_finder.py`
- OpenAI API integration
- Manufacturer research
- Credibility scoring
- Detailed analysis generation

### `excel_exporter.py`
- Exports results to Excel
- Applies formatting and styles
- Color-codes credibility scores
- Creates summary sheets

### `main.py`
- Command-line orchestrator
- Workflow management
- Logging and error handling

### `app.py`
- Streamlit web interface
- Interactive UI
- Real-time progress tracking
- Download capabilities

## 🎯 Use Cases

- **Procurement Teams**: Research suppliers for new parts
- **Supply Chain Managers**: Validate manufacturer credibility
- **Quality Assurance**: Assess manufacturer quality and reliability
- **Product Development**: Find manufacturers for custom parts
- **Cost Analysis**: Compare multiple manufacturer options

## ⚙️ Configuration

### OpenAI Model Settings
The tool uses `gpt-4o-mini` by default for cost-effectiveness. You can modify this in `manufacturer_finder.py`:

```python
model="gpt-4o-mini"  # Change to "gpt-4" for enhanced accuracy
```

### Analysis Parameters
- **Max Manufacturers**: Number of manufacturers to recommend per item (default: 5)
- **Temperature**: AI creativity level (default: 0.7)
- **Max Tokens**: Response length limit (default: 1500)

## 📝 Logging

All operations are logged to `manufacturer_finder.log` with timestamps, including:
- Data loading events
- API calls
- Errors and warnings
- Analysis progress

## 🐛 Troubleshooting

### "OpenAI API key not provided"
- Set the `OPENAI_API_KEY` environment variable
- Or provide via `--api-key` flag
- Or enter in the web UI sidebar

### "Missing required column"
- Ensure Excel has MPN, Description, and Quantity columns
- Column names are auto-detected but should contain keywords like "MPN", "Description", "Quantity"

### "Rate limit exceeded"
- The tool includes automatic rate limiting (0.5s between requests)
- If you hit limits, wait a few minutes and retry
- Consider upgrading your OpenAI plan for higher limits

### Excel File Errors
- Ensure file is `.xlsx` or `.xls` format
- Check that data starts from row 1 with headers
- Remove any merged cells or complex formatting

## 💡 Tips for Best Results

1. **Detailed Descriptions**: Provide comprehensive model descriptions for better manufacturer matches
2. **Accurate MPNs**: Use official manufacturer part numbers when available
3. **Realistic Quantities**: Include accurate quantities as they affect manufacturer recommendations
4. **Review Low Scores**: Items with credibility scores <60 may need manual verification
5. **Check Multiple Results**: Review all recommended manufacturers, not just the top one

## 🔒 Security

- API keys are never logged or stored
- Use environment variables for API key management
- All file operations are logged for audit trails

## 📊 Performance

- Processing time: ~2-5 seconds per item
- Batch processing: Analyzes all items sequentially
- Rate limiting: 0.5s delay between API calls to prevent rate limits

## 🤝 Support

For issues or questions:
1. Check the logs: `manufacturer_finder.log`
2. Verify Excel file format
3. Ensure OpenAI API key is valid and has credits
4. Review error messages for specific guidance

## 📜 License

This tool is provided as-is for internal use at DynaPrice.

## 🔄 Version History

- **v1.0.0** (Current): Initial release with full functionality
  - Excel data loading
  - OpenAI GPT-4 integration
  - Credibility scoring
  - Streamlit web interface
  - Formatted Excel export

---

**Built with ❤️ for DynaPrice Internship Project**
