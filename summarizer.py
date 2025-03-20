from transformers import pipeline

# Load the summarization model
summarizer = pipeline("summarization")

def summarize_email(email_text):
    # Ensure the input is not too long
    max_input = 1024  # Adjust based on model limitations
    email_text = email_text[:max_input]

    # Generate summary
    summary = summarizer(email_text, max_length=150, min_length=50, do_sample=False)

    return summary[0]['summary_text']
