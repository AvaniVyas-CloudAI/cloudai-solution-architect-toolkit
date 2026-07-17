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
    if not business_problem.strip():

        st.warning("Please describe the business problem before generating the solution brief.")

        st.stop()
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

    st.write(f"Selected security level: {security_level}")

    if security_level == "Low":
        st.write("- Use approved data sources only")
        st.write("- Restrict access to the application")
        st.write("- Avoid storing sensitive customer or internal data in the first version")
        st.write("- Review generated answers before using them in production")

    elif security_level == "Medium":
        st.write("- Use role-based access control for different user types")
        st.write("- Store documents in a secure cloud storage location")
        st.write("- Encrypt data where possible")
        st.write("- Log important user actions and application errors")
        st.write("- Add review steps for unclear or sensitive answers")

    else:
        st.write("- Use strict identity and access management controls")
        st.write("- Encrypt data at rest and in transit")
        st.write("- Avoid exposing sensitive data directly to the model")
        st.write("- Add audit logging for user activity and generated outputs")
        st.write("- Add human review for risky, sensitive, or customer-facing answers")
        st.write("- Consider compliance needs before production use")

    st.subheader("Cost Considerations")

    st.write(f"Selected budget sensitivity: {budget_sensitivity}")

    if budget_sensitivity == "High":
        st.write("- Start with a small prototype before scaling")
        st.write("- Keep model/API usage limited during early testing")
        st.write("- Use cost alerts and usage limits")
        st.write("- Reuse existing documents and cloud resources where possible")
        st.write("- Avoid over-engineering the first version")

    elif budget_sensitivity == "Medium":
        st.write("- Balance cost control with reliability")
        st.write("- Use managed cloud services where they reduce maintenance effort")
        st.write("- Track storage, hosting, and model/API usage")
        st.write("- Review costs before increasing users or document volume")
        st.write("- Scale gradually after the MVP proves value")

    else:
        st.write("- Prioritize performance, reliability, and scalability")
        st.write("- Plan for stronger infrastructure and monitoring")
        st.write("- Use higher-capacity services if response speed is important")
        st.write("- Track cost trends even if performance is the main priority")
        st.write("- Review architecture regularly as usage grows")

    st.subheader("Observability Considerations")
    st.write("- Track failed or low-quality answers")
    st.write("- Monitor response time")
    st.write("- Collect user feedback")
    st.write("- Review logs regularly")
    st.subheader("User Scale Recommendation")

    st.write(f"Expected users: {expected_users}")

    if expected_users <= 100:
        st.write("- Start with a simple MVP setup")
        st.write("- A lightweight Streamlit app is enough for early testing")
        st.write("- Use basic logging and manual review")
        st.write("- Avoid complex infrastructure until the use case is validated")

    elif expected_users <= 1000:
        st.write("- Plan for a more structured backend as usage grows")
        st.write("- Add authentication and role-based access")
        st.write("- Use centralized logging and basic monitoring")
        st.write("- Prepare the app for deployment on a managed cloud service")

    else:
        st.write("- Design for scalability from the beginning")
        st.write("- Use a dedicated backend service instead of only a local app")
        st.write("- Add rate limits, monitoring, error tracking, and access control")
        st.write("- Plan for cloud deployment, performance testing, and cost tracking")
    st.subheader("Risk Level")

    if security_level == "High" or expected_users > 1000:
        st.write("Estimated risk level: High")
        st.write(
            "This solution may involve sensitive data, high usage, or customer-facing impact. "
            "It should include strong access control, audit logging, human review, and careful testing before production use."
        )

    elif security_level == "Medium" or expected_users > 100:
        st.write("Estimated risk level: Medium")
        st.write(
            "This solution has moderate risk because it may involve internal documents, multiple users, or operational decisions. "
            "It should include role-based access, monitoring, and review steps before wider rollout."
        )

    else:
        st.write("Estimated risk level: Low")
        st.write(
            "This solution is suitable for early MVP testing with limited users and low-sensitive data. "
            "Start small, test the output quality, and improve controls as the solution grows."
        )

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
