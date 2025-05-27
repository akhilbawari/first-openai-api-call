# First OpenAI API Call

A simple Python script that demonstrates how to make a successful API call to OpenAI's GPT-3.5-turbo model and display the response with token usage information.

## What This Script Does

- Makes an API call to OpenAI's GPT-3.5-turbo model
- Uses a fixed system prompt to set the assistant's behavior
- Takes user input via console
- Displays the assistant's response
- Shows detailed token usage statistics (prompt tokens, completion tokens, total tokens)

## Prerequisites

- Python 3.7+
- OpenAI API key (see setup instructions below)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/akhilbawari/first-openai-api-call.git
cd first-openai-api-call
```

### 2. Install Dependencies

```bash
pip install openai
```

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key

**Important: Never commit your API key to version control!**

Set your OpenAI API key as an environment variable:

**On macOS/Linux:**
```bash
export OPENAI_API_KEY='your-api-key-here'
```

**On Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-api-key-here
```

**On Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

### 4. Run the Script

```bash
python first_call.py
```

## Usage Example

```
🚀 OpenAI API Call Demo
==============================

📝 Enter your prompt (press Enter when done):
> What is the capital of France?

⏳ Making API call...

==================================================
🤖 ASSISTANT RESPONSE:
==================================================
The capital of France is Paris. It is located in the north-central part of the country and serves as the political, economic, and cultural center of France.

==================================================
📊 TOKEN USAGE:
==================================================
Prompt tokens: 23
Completion tokens: 28
Total tokens: 51
==================================================
```

## Features

- ✅ Console-based user input
- ✅ Fixed system prompt
- ✅ Error handling for missing API key
- ✅ Detailed token usage display
- ✅ Clean, formatted output
- ✅ Secure API key handling (environment variable)

## File Structure

```
first-openai-api-call/
├── first_call.py          # Main script
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore           # Git ignore file (excludes API keys)
```

## Security Notes

- **Never commit your API key** to version control
- Store your API key in environment variables
- The `.gitignore` file is configured to exclude common files that might contain API keys

## Getting Help

If you encounter issues:

1. Make sure your API key is set correctly
2. Check your internet connection
3. Verify you have sufficient API credits
4. Check the OpenAI API status page

