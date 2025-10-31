# 🚀 START HERE - Manufacturer Finder Tool

Welcome to the **Manufacturer Finder Tool**! This guide will help you get started in minutes.

---

## 🎯 What This Tool Does

This tool uses **OpenAI's GPT-4** to analyze your manufacturing parts and recommend **credible manufacturers** based on:
- ✅ Industry reputation
- ✅ Product quality  
- ✅ Supply chain reliability
- ✅ Market presence

You provide an Excel file with **MPN**, **Model Description**, and **Quantity**, and get back manufacturer recommendations with credibility scores!

---

## ⚡ Quick Start (3 Steps)

### Step 1: Install Dependencies

Open your terminal in this folder and run:

```bash
pip install -r requirements.txt
```

### Step 2: Set Your OpenAI API Key

**Option A** - Environment Variable (easiest):
```bash
export OPENAI_API_KEY='your-api-key-here'
```

**Option B** - Create a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

**Option C** - Enter it in the web interface when you launch the app

> 🔑 Don't have an API key? Get one at https://platform.openai.com/api-keys

### Step 3: Launch the Tool

**Web Interface** (Recommended):
```bash
streamlit run app.py
```

Or use the quick launch script:
```bash
./run_app.sh
```

**Command Line**:
```bash
python main.py your_data.xlsx
```

---

## 📊 Prepare Your Excel File

Your Excel file should have these columns:

| MPN | Model Description | Quantity |
|-----|------------------|----------|
| ABC-12345 | Industrial servo motor 5HP | 100 |
| XYZ-67890 | Precision bearing assembly | 250 |

> 💡 See `example_input.xlsx` for a sample file you can use to test!

**Column names are auto-detected**, so variations like "Part Number", "Description", "Qty" will work.

---

## 🖥️ Using the Web Interface

1. **Open your browser** to http://localhost:8501
2. **Enter your API key** in the sidebar (if not set as environment variable)
3. **Upload your Excel file**
4. **Click "Start Analysis"** and wait for the AI to work its magic
5. **Download results** - you'll get a formatted Excel file with:
   - 🏆 Top manufacturer recommendations
   - 📊 Credibility scores (color-coded)
   - 📝 Detailed analysis for each manufacturer

---

## 📥 What You Get

### Output Excel File Contains:

**Summary Sheet:**
- Quick overview with top manufacturer and credibility score

**Detailed Analysis Sheet:**
- All manufacturers found
- Credibility scores (0-100)
- Strengths and considerations for each
- Recommendations and additional info

**Color Coding:**
- 🟢 **Green (≥80)**: High credibility, excellent choice
- 🟡 **Yellow (60-79)**: Medium credibility, good option
- 🔴 **Red (<60)**: Low credibility, needs review

---

## 💡 Pro Tips

✅ **Be Specific**: More detailed product descriptions = better manufacturer matches

✅ **Accurate MPNs**: Use official manufacturer part numbers when possible

✅ **Check Multiple Results**: Review all recommended manufacturers, not just #1

✅ **Low Scores?**: Items scoring <60 may need manual verification

✅ **Batch Processing**: Analyze multiple parts at once to save time

---

## 🔧 Troubleshooting

### "OpenAI API key not provided"
→ Set `OPENAI_API_KEY` environment variable or enter in the UI

### "Missing required column"  
→ Ensure your Excel has MPN, Description, and Quantity columns

### "Rate limit exceeded"
→ Wait a few minutes and retry. The tool includes automatic rate limiting.

### Module not found errors
→ Run `pip install -r requirements.txt` again

---

## 📖 Need More Help?

- **Detailed documentation**: See `README.md`
- **Quick reference**: See `HOW_TO_RUN.txt`  
- **Check logs**: See `manufacturer_finder.log` for error details
- **Example file**: Use `example_input.xlsx` to test the tool

---

## 🎓 Example Workflow

1. **Prepare** your Excel file with parts data
2. **Launch** the web app: `streamlit run app.py`
3. **Upload** your file and click "Start Analysis"
4. **Review** results in the interactive table
5. **Download** the formatted Excel report
6. **Share** findings with your team!

---

## 🚀 You're Ready!

Everything is set up and ready to use. Just:

1. Install dependencies: `pip install -r requirements.txt`
2. Set your API key: `export OPENAI_API_KEY='your-key'`
3. Launch the app: `streamlit run app.py`
4. Upload your Excel and analyze!

**Happy manufacturer hunting! 🏭**

---

*Built for DynaPrice Internship Project*

