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
- OpenAI API key
- CSV file for analysis

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd analyst_project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Prepare your data**
   - Place your CSV file in the project directory
   - Update `CSV_FILE_PATH` in `my_server.py` if needed
   - Default file: `Online Sales Data.csv`

### Running the Server

```bash
python my_server.py
```

The server will start and be ready to accept MCP connections.

## 📋 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Required for AI analysis features
- `CSV_FILE_PATH`: Path to your CSV file (default: `Online Sales Data.csv`)
- `TABLE_NAME`: Name used for SQL table operations (default: `data`)

### Server Settings
- **Temperature**: Set to 0.3 for consistent, focused AI responses
- **Max Tokens**: Limited to 1000 for efficient responses
- **Data Truncation**: Automatically limits data to 4000 characters for API limits

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
- Add your API key to `.env` file
- Restart the server after updating

**Rate limit errors**
- Wait a moment between requests
- Reduce data size in queries
- Check OpenAI billing status

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

```
pandas>=1.3.0
numpy>=1.21.0
fastmcp>=0.1.0
duckdb>=0.8.0
tabulate>=0.9.0
openai>=1.0.0
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
