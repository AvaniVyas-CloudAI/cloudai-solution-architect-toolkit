import streamlit as st

st.set_page_config(
    page_title="CloudAI Solution Architect Toolkit",
    page_icon="☁️",
    layout="wide"
)

st.title("CloudAI Solution Architect Toolkit")

st.write(
    "A learning-focused tool that converts a business problem into a basic AI/cloud solution brief."
)

st.divider()

st.header("Business Problem Input")

industry = st.selectbox(
    "Industry",
    [
        "SaaS",
        "Healthcare",
        "Banking",
        "Retail",
        "Education",
        "Manufacturing",
        "Other"
    ]
)

business_problem = st.text_area(
    "Describe the business problem",
    placeholder="Example: A support team receives repeated customer questions and wants to reduce manual effort."
)

cloud_preference = st.selectbox(
    "Cloud preference",
    [
        "AWS",
        "GCP",
        "Azure",
        "No preference"
    ]
)

data_sources = st.multiselect(
    "Available data sources",
    [
        "Product documentation",
        "FAQs",
        "Support tickets",
        "Internal policies",
        "Knowledge base articles",
        "Customer emails",
        "Release notes"
    ]
)

security_level = st.selectbox(
    "Security level",
    [
        "Low",
        "Medium",
        "High"
    ]
)

budget_sensitivity = st.selectbox(
    "Budget sensitivity",
    [
        "Low",
        "Medium",
        "High"
    ]
)

expected_users = st.number_input(
    "Expected number of users",
    min_value=1,
    value=50
)

desired_outcome = st.text_area(
    "Desired outcome",
    placeholder="Example: Faster response time, reduced repetitive work, and improved answer consistency."
)

st.divider()

if st.button("Generate Solution Brief"):
    st.header("Generated AI/Cloud Solution Brief")

    st.subheader("Problem Summary")
    st.write(
        f"The organization operates in the {industry} industry and is facing the following problem:"
    )
    st.write(business_problem)

    st.subheader("Recommended AI Use Case")
    st.write(
        "A suitable first AI use case is an assistant that can help users find answers from trusted business knowledge sources."
    )
    st.subheader("Knowledge Sources")

    if data_sources:
        st.write("The solution can use the following available data sources:")
        for source in data_sources:
            st.write(f"- {source}")
    else:
        st.write(
            "No data sources were selected. A real AI solution would need trusted documents, knowledge bases, or business data before it can generate reliable answers."
        )
            st.subheader("Desired Business Outcome")

    if desired_outcome:
        st.write(desired_outcome)
    else:
        st.write(
            "No desired outcome was provided. A strong AI/cloud solution should clearly define what business result it is trying to improve."
        )
    st.subheader("Suggested Architecture Approach")
    st.write(
        "The first version should use a simple input interface, a document knowledge layer, an AI model for response generation, and basic monitoring."
    )
    st.subheader("Architecture Flow")

    st.write(
        "User Input → Business Problem Analysis → Knowledge Sources → AI/Cloud Solution Brief → Review and Improvement"
    )
    st.subheader("Cloud Services to Consider")

    if cloud_preference == "AWS":
        st.write("- Amazon S3 for document storage")
        st.write("- Amazon Bedrock for model access")
        st.write("- AWS Lambda or ECS for backend processing")
        st.write("- Amazon CloudWatch for logs and monitoring")
    elif cloud_preference == "GCP":
        st.write("- Cloud Storage for document storage")
        st.write("- Vertex AI for model access")
        st.write("- Cloud Run for application hosting")
        st.write("- Cloud Logging and Monitoring")
    elif cloud_preference == "Azure":
        st.write("- Azure Blob Storage for document storage")
        st.write("- Azure OpenAI Service for model access")
        st.write("- Azure App Service or Azure Functions for hosting")
        st.write("- Azure Monitor for logs and monitoring")
    else:
        st.write("- Cloud storage for documents")
        st.write("- Managed AI model service")
        st.write("- Serverless or container-based hosting")
        st.write("- Logging and monitoring service")

    st.subheader("Security Considerations")
    if security_level == "High":
        st.write("- Use strict role-based access control")
        st.write("- Avoid exposing sensitive data to the model")
        st.write("- Add human review for risky or customer-facing answers")
        st.write("- Log only necessary information")
    else:
        st.write("- Use approved data sources")
        st.write("- Control access to internal documents")
        st.write("- Review uncertain answers before production use")

    st.subheader("Cost Considerations")
    if budget_sensitivity == "High":
        st.write("- Start with a small document set")
        st.write("- Limit model usage during early testing")
        st.write("- Use cost alerts")
        st.write("- Avoid over-engineering the first version")
    else:
        st.write("- Monitor model usage")
        st.write("- Track hosting and storage costs")
        st.write("- Review costs before scaling to more users")

    st.subheader("Observability Considerations")
    st.write("- Track failed or low-quality answers")
    st.write("- Monitor response time")
    st.write("- Collect user feedback")
    st.write("- Review logs regularly")

    st.subheader("Implementation Approach")
    st.write(
        "Start with a small prototype using a limited set of trusted documents. Improve retrieval quality, security, and monitoring before expanding to more users."
    )
        st.subheader("Suggested First Steps")

    st.write("- Confirm the business problem and expected outcome")
    st.write("- Identify trusted data sources that can be used safely")
    st.write("- Build a small prototype with limited users")
    st.write("- Review output quality before expanding access")
    st.write("- Add monitoring, feedback, and cost controls")
