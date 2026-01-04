# 📊 Data Analyst MCP Server

A powerful Model Context Protocol (MCP) server that provides comprehensive data analysis capabilities for CSV files. This server acts as an intelligent data analyst agent, enabling SQL queries and AI-powered insights.

## 🌟 Features

### Core Capabilities
- **Data Schema Inspection**: Automatically analyze CSV structure, data types, and statistics
- **SQL Query Engine**: Full DuckDB integration for complex data analysis
- **AI-Powered Analysis**: OpenAI integration for intelligent data insights and recommendations

### Available Tools
1. **`get_data_schema`** - Comprehensive data structure analysis
2. **`run_sql_query`** - Execute SQL queries on your data
3. **`analyze_with_ai`** - AI-powered data analysis with structured output

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (required for AI analysis features)
- CSV file for analysis

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd analyst_project
   ```

2. **Install dependencies**
   ```bash
   pip install fastmcp pandas numpy duckdb openai python-dotenv matplotlib seaborn
   ```
   
   *Alternatively, create a requirements.txt file:*
   ```
   fastmcp>=2.14.0
   pandas>=1.3.0
   numpy>=1.21.0
   duckdb>=0.8.0
   openai>=1.0.0
   python-dotenv>=0.19.0
   matplotlib>=3.5.0
   seaborn>=0.11.0
   ```

3. **Set up OpenAI API key**
   
   **Option A: Using .env file (Recommended)**
   ```bash
   # Create a .env file
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```
   
   **Option B: Set environment variable directly**
   ```bash
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="your_openai_api_key_here"
   
   # Windows (Command Prompt)
   set OPENAI_API_KEY=your_openai_api_key_here
   
   # macOS/Linux
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```
   
   **How to get your OpenAI API key:**
   1. Go to [OpenAI Platform](https://platform.openai.com/)
   2. Sign up or log in to your account
   3. Navigate to **API Keys** in the sidebar
   4. Click "Create new secret key"
   5. Copy the key and save it securely
   6. Add credits to your account (minimum $5 required)

4. **Prepare your data**
   - Place your CSV file in the project directory
   - Update `CSV_FILE_PATH` in `my_server.py` if needed
   - Default file: `Online Sales Data.csv`

### Running the Server

```bash
python my_server.py
```

The server will start and be ready to accept MCP connections.

## 🧪 Testing Your Setup

### Quick Test with Client
Use the provided test client to verify everything works:

```bash
python open_ai_connectivity_test.py
```

This will:
1. Test the server connection
2. Verify data schema analysis
3. Test AI analysis functionality

### Manual Testing Steps
1. **Start the server**: `python my_server.py`
2. **Check server logs**: Look for "Started server process" message
3. **Test with client**: Run `python open_ai_connectivity_test.py` in another terminal
4. **Verify output**: You should see schema data and AI analysis results

### Expected Output
```
============================================================
Testing Data Analyst MCP Server
============================================================

1. Testing get_data_schema()...
{
  "table_name": "data",
  "columns": [...],
  "row_count": 240,
  ...
}

4. Testing analyze_with_ai (Direct Call)...
- summary
[AI-generated summary of your data]

- insights  
[Key patterns and observations]

- recommendations
[Actionable suggestions]
```

## 📋 Configuration

### Environment Variables
- `OPENAI_API_KEY`: **Required** for AI analysis features (see setup above)
- `CSV_FILE_PATH`: Path to your CSV file (default: `Online Sales Data.csv`)
- `TABLE_NAME`: Name used for SQL table operations (default: `data`)

### OpenAI Configuration
- **Model**: Uses `gpt-4o-mini` for cost-effective analysis
- **Temperature**: Set to 0.3 for consistent, focused responses
- **Max Tokens**: Limited to 1000 for efficient responses
- **Data Limits**: Automatically truncates data to 4000 characters to stay within API limits
- **Cost**: Approximately $0.15 per 1M tokens (very affordable for data analysis)

## 🔧 Available Tools

### 1. get_data_schema()
**Purpose**: Analyze CSV structure and metadata
**Returns**: JSON with table name, columns, row count, and column details
**Use Case**: Always run first to understand your data

```python
# Example output
{
    "table_name": "Online Sales Data",
    "columns": ["Region", "Product", "Sales", "Date"],
    "row_count": 1000,
    "column_details": {
        "Sales": {
            "data_type": "float64",
            "min": 10.5,
            "max": 500.0,
            "sample_values": [25.0, 45.5, 100.0]
        }
    }
}
```

### 2. run_sql_query(query: str)
**Purpose**: Execute SQL queries using DuckDB
**Parameters**: SQL query string
**Returns**: Formatted table results

```sql
-- Example queries
SELECT Region, SUM(Sales) as TotalSales FROM data GROUP BY Region
SELECT Product, COUNT(*) as Orders FROM data WHERE Sales > 100 GROUP BY Product
SELECT * FROM data ORDER BY Sales DESC LIMIT 10
```

### 3. analyze_with_ai(data_context: str, user_question: str = "")
**Purpose**: AI-powered data analysis with structured output
**Parameters**: 
- `data_context`: Data to analyze
- `user_question`: Specific analysis question (optional)

**Returns**: Formatted string with three sections:
```
- summary
[Brief overview of key findings]

- insights
[Detailed observations and patterns]

- recommendations
[Actionable suggestions based on analysis]
```

## 💡 Usage Examples

### Basic Data Exploration
```python
# 1. First, understand the data structure
schema = get_data_schema()

# 2. Run basic queries
results = run_sql_query("SELECT COUNT(*) as total_records FROM data")

# 3. Get AI insights
insights = analyze_with_ai(results, "What are the key patterns in this data?")
```

### Typical Workflow
1. **Start with schema analysis**: `get_data_schema()`
2. **Explore with SQL**: `run_sql_query()` for specific questions
3. **Get AI insights**: `analyze_with_ai()` for deeper understanding

## 📊 Supported Data Types

The server automatically handles:
- **Numeric data**: Integers, floats with min/max statistics
- **Categorical data**: Unique counts and sample values
- **Text data**: Sample values and character analysis
- **Date/Time**: Automatic parsing and temporal analysis

## 🛠️ Technical Architecture

### Core Components
- **FastMCP**: MCP server framework
- **Pandas**: Data manipulation and analysis
- **DuckDB**: In-memory SQL database
- **OpenAI GPT-4o-mini**: AI analysis engine

### Data Flow
1. CSV → Pandas DataFrame
2. DataFrame → DuckDB in-memory table
3. SQL queries → DuckDB execution
4. Results → OpenAI analysis (optional)
5. Formatted output → MCP response

## 🔒 Safety & Limits

### API Protection
- **Data truncation**: Automatically limits to 4000 characters
- **Rate limiting**: Graceful handling of OpenAI rate limits
- **Error handling**: Comprehensive error messages and fallbacks

### Security Considerations
- Environment variables for API keys
- Input validation for SQL queries
- Safe file operations with error handling

## 🐛 Troubleshooting

### Common Issues

**"CSV file not found"**
- Check `CSV_FILE_PATH` in `my_server.py`
- Ensure CSV file exists in the correct location

**"OPENAI_API_KEY not set"**
- Ensure you've set up your API key using one of the methods above
- Verify the .env file exists and contains your key
- Restart the server after updating environment variables
- Check that your OpenAI account has credits available

**Rate limit errors**
- OpenAI has rate limits (typically 60 requests/minute for gpt-4o-mini)
- Wait a moment between requests if you hit limits
- Reduce data size in queries (server auto-truncates to 4000 chars)
- Check your OpenAI billing and usage
- Consider upgrading your account for higher limits

**SQL query errors**
- Use correct table name (`data` by default)
- Check column names from schema first
- Validate SQL syntax

### Debug Mode
The server includes debug prints for AI analysis:
- Data length tracking
- Truncation notifications
- API response status

## 📦 Dependencies

### Core Dependencies
```bash
fastmcp>=2.14.0      # MCP server framework
pandas>=1.3.0        # Data manipulation
numpy>=1.21.0        # Numerical operations
duckdb>=0.8.0        # In-memory SQL database
openai>=1.0.0        # OpenAI API client
python-dotenv>=0.19.0 # Environment variable management
```

### Optional Dependencies (for enhanced features)
```bash
matplotlib>=3.5.0    # Chart generation (future feature)
seaborn>=0.11.0      # Statistical visualization
```

### Installation Command
```bash
pip install fastmcp pandas numpy duckdb openai python-dotenv matplotlib seaborn
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔮 Future Enhancements

- [ ] Add chart generation functionality
- [ ] Add support for multiple CSV files
- [ ] Implement data caching for performance
- [ ] Add more AI analysis templates
- [ ] Support for additional database backends
- [ ] Web interface for non-MCP usage

## 📞 Support

For issues, questions, or contributions:
- Create an issue in the repository
- Check the troubleshooting section above
- Review the debug output for detailed error information

---

**Built with ❤️ for data analysts and developers**
