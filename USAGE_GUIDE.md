# 🎯 Usage Guide - Manufacturer Finder Tool

## ✅ Your API Key is Set Up and Working!

Test completed successfully with **95/100 average credibility score** on sample data.

---

## 🚀 Quick Start Options

### Option 1: Web Interface (Easiest!)

```bash
python3 quick_start.py
# Then choose option 1
```

Or directly:
```bash
streamlit run app.py
```

This opens a beautiful web interface where you can:
- Upload Excel files with drag-and-drop
- See real-time progress
- View interactive results
- Download formatted reports

### Option 2: Command Line

For a single Excel file:
```bash
python3 quick_start.py
# Then choose option 2
```

Or directly:
```bash
python3 main.py your_data.xlsx
```

---

## 📊 Excel File Format

Your Excel file should have these columns:

| MPN | Model Description | Quantity |
|-----|------------------|----------|
| ABC-12345 | Industrial servo motor 5HP | 100 |
| XYZ-67890 | Precision bearing assembly | 250 |

**Supported column names:**
- **MPN**: `MPN`, `Part Number`, `PartNumber`
- **Description**: `Model`, `Description`, `Product`, `Model Description`  
- **Quantity**: `Quantity`, `Qty`, `Amount`

---

## 🎯 Real-World Example

Based on our test run, here's what you get:

**Input:**
```
MPN: ABC-12345
Description: Industrial servo motor 5HP with encoder
Quantity: 100
```

**Output:**
```
Top Manufacturer: Siemens
Credibility Score: 94/100
Other Options: Rockwell Automation, Yaskawa, Mitsubishi

Recommendation: Siemens is the top recommendation due to 
its industry leadership, exceptional product quality, and 
extensive support network, making it an ideal choice for 
critical applications.
```

---

## 📥 What You Get

Your analysis creates an Excel file with two sheets:

### 1. Summary Sheet
Quick overview with:
- MPN
- Model Description  
- Top Manufacturer
- Credibility Score (color-coded)

### 2. Detailed Analysis Sheet
Complete analysis with:
- All manufacturers found (3-5 per item)
- Individual credibility scores
- Strengths for each manufacturer
- Considerations (MOQ, lead times, certifications)
- Recommendations

**Color Coding:**
- 🟢 Green (≥80): High credibility - Excellent choice
- 🟡 Yellow (60-79): Medium credibility - Good option  
- 🔴 Red (<60): Low credibility - Needs review

---

## 💡 Usage Examples

### Example 1: Analyze Your Data
```bash
# Place your Excel file in the folder, then:
python3 main.py my_parts.xlsx
```

### Example 2: Custom Output Name
```bash
python3 main.py my_parts.xlsx --output my_results.xlsx
```

### Example 3: Limit Manufacturers
```bash
# Get only top 3 manufacturers per item
python3 main.py my_parts.xlsx --max-manufacturers 3
```

### Example 4: Web Interface (Best for Multiple Runs)
```bash
streamlit run app.py
# Upload different files, compare results, download reports
```

---

## 📋 Step-by-Step Workflow

### For Your Own Data:

1. **Prepare Excel File**
   - Create columns: MPN, Model Description, Quantity
   - Add your parts data
   - Save as .xlsx file

2. **Run Analysis**
   ```bash
   python3 quick_start.py
   # Choose option 2, enter your filename
   ```

3. **Review Results**
   - Open the generated Excel file
   - Check Summary sheet for quick overview
   - Review Detailed Analysis for full information

4. **Make Decisions**
   - High scores (≥80): Reliable manufacturers
   - Medium scores (60-79): Worth considering
   - Low scores (<60): Need additional verification

---

## 🎓 Tips for Best Results

✅ **Be Specific**: More detailed descriptions = better matches
   - Good: "Industrial servo motor 5HP 480V with absolute encoder"
   - Basic: "Motor"

✅ **Use Real MPNs**: Official part numbers get better results

✅ **Include Quantity**: Affects manufacturer recommendations
   - Large orders (>1000): May suggest different manufacturers
   - Small orders: More flexible options

✅ **Review All Options**: Don't just look at #1 manufacturer

✅ **Check Considerations**: Pay attention to MOQ, lead times, certifications

---

## 🔧 Common Tasks

### Analyze Multiple Files
```bash
python3 main.py file1.xlsx --output results1.xlsx
python3 main.py file2.xlsx --output results2.xlsx
python3 main.py file3.xlsx --output results3.xlsx
```

### Compare Different Quantities
Create multiple Excel files with different quantities and compare recommendations.

### Focus on Specific Categories
Filter your Excel to analyze only certain types of parts (motors, bearings, etc.)

---

## 📊 Understanding the Results

### Credibility Score Breakdown

**90-100**: Industry leaders
- Top-tier manufacturers
- Proven track record
- Extensive support

**80-89**: Excellent options  
- Strong reputation
- Good quality
- Reliable supply chain

**70-79**: Good choices
- Established manufacturers
- Decent reputation
- May have some limitations

**60-69**: Acceptable
- Known manufacturers
- Check specific requirements
- Verify capabilities

**<60**: Proceed with caution
- Less established
- Limited information
- Additional verification needed

---

## 🚀 Your Next Steps

1. **Prepare your Excel file** with your actual parts data

2. **Choose your method:**
   - **Quick & Easy**: `python3 quick_start.py`
   - **Web Interface**: `streamlit run app.py`  
   - **Command Line**: `python3 main.py your_file.xlsx`

3. **Analyze and review** the manufacturer recommendations

4. **Use the insights** for procurement decisions

---

## 📞 Need Help?

- **Quick help**: `python3 quick_start.py` → Choose option 4
- **Full docs**: See `README.md`
- **Examples**: Run `python3 example_usage.py`
- **Logs**: Check `manufacturer_finder.log` for detailed info

---

**Your tool is ready to use! Happy manufacturer hunting! 🏭**

