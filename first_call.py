#!/usr/bin/env python3
"""
First OpenAI API Call Script
Makes a successful API call to OpenAI's GPT-3.5-turbo model
and displays the response with token usage information.
"""

import os
import sys
from openai import OpenAI

def setup_client():
    """Initialize OpenAI client with API key from environment variable"""
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable not found!")
        print("Please set your API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    return OpenAI(api_key=api_key)

def make_api_call(client, user_prompt):
    """Make API call to OpenAI GPT-3.5-turbo model"""
    
    # Fixed system prompt as required
    system_prompt = "You are a helpful assistant that provides clear, concise, and accurate responses."
    
    try:
        # Make the API call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        return response
    
    except Exception as e:
        print(f"❌ API call failed: {e}")
        sys.exit(1)

def display_results(response):
    """Display the assistant's response and token usage"""
    
    # Extract response content
    assistant_reply = response.choices[0].message.content
    
    # Extract token usage
    token_usage = response.usage
    
    print("\n" + "="*50)
    print("🤖 ASSISTANT RESPONSE:")
    print("="*50)
    print(assistant_reply)
    
    print("\n" + "="*50)
    print("📊 TOKEN USAGE:")
    print("="*50)
    print(f"Prompt tokens: {token_usage.prompt_tokens}")
    print(f"Completion tokens: {token_usage.completion_tokens}")
    print(f"Total tokens: {token_usage.total_tokens}")
    print("="*50)

def main():
    """Main function to run the OpenAI API call"""
    
    print("🚀 OpenAI API Call Demo")
    print("="*30)
    
    # Setup OpenAI client
    client = setup_client()
    
    # Get user input
    print("\n📝 Enter your prompt (press Enter when done):")
    user_prompt = input("> ")
    
    if not user_prompt.strip():
        print("❌ Empty prompt provided. Exiting...")
        sys.exit(1)
    
    print("\n⏳ Making API call...")
    
    # Make API call
    response = make_api_call(client, user_prompt)
    
    # Display results
    display_results(response)

if __name__ == "__main__":
    main()