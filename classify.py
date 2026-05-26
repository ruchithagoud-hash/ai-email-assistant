def classify_email(subject, snippet):
    text = f"{subject} {snippet}".lower()

    # 1. Spam detection
    spam_keywords = [
        "lottery", "win money", "free gift", "claim prize",
        "urgent payment", "winner"
    ]
    if any(word in text for word in spam_keywords):
        return "SPAM"

    # 2. Important & Urgent detection
    urgent_keywords = [
        "urgent", "deadline", "asap", "tomorrow",
        "immediately", "last date"
    ]
    if any(word in text for word in urgent_keywords):
        return "Important-Urgent"

    # 3. Important but General
    important_keywords = [
        "important", "alert", "notice", "policy update"
    ]
    if any(word in text for word in important_keywords):
        return "Important-General"

    # 4. Work-related (now includes tech-related terms)
    work_keywords = [
        "project", "meeting", "report", "client", "invoice", "team",
        "job", "hiring", "developer", "engineer", "codeforces", "coding",
        "programming", "udemy", "course", "linkedin", "interview", "career",
        "software", "technology", "ai", "machine learning", "data science"
    ]
    if any(word in text for word in work_keywords):
        return "Works"

    # 5. Personal
    personal_keywords = [
        "birthday", "party", "dinner", "family", "friend", "congratulations"
    ]
    if any(word in text for word in personal_keywords):
        return "Personals"

    # Default if nothing matches
    return "Others"
