import streamlit as st
from groq import Groq
import re

# Initialize the Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

competencies_list = """"
<competency definitions>
K1
Knowledge
How to use ai and machine learning methodologies such as data-mining, supervised/unsupervised machine learning, natural language processing, machine vision to meet business objectives

K2
Knowledge
How to apply modern data storage solutions, processing technologies and machine learning methods to maximise the impact to the organisation by drawing conclusions from applied research

K3
Knowledge
How to apply advanced statistical and mathematical methods to commercial projects

K4
Knowledge
How to extract data from systems and link data from multiple systems to meet business objectives

K5
Knowledge
How to design and deploy effective techniques of data analysis and research to meet the needs of the business and customers

K6
Knowledge
How data products can be delivered to engage the customer, organise information or solve a business problem using a range of methodologies, including iterative and incremental development and project management approaches

K7
Knowledge
How to solve problems and evaluate software solutions via analysis of test data and results from research, feasibility, acceptance and usability testing

K8
Knowledge
How to interpret organisational policies, standards and guidelines in relation to ai and data

K9
Knowledge
The current or future legal, ethical, professional and regulatory frameworks which affect the development, launch and ongoing delivery and iteration of data products and services.

K10
Knowledge
How own role fits with, and supports, organisational strategy and objectives

K11
Knowledge
The roles and impact of ai, data science and data engineering in industry and society

K12
Knowledge
The wider social context of ai, data science and related technologies, to assess business impact of current ethical issues such as workplace automation and misuse of data

K13
Knowledge
How to identify the compromises and trade-offs which must be made when translating theory into practice in the workplace

K14
Knowledge
The business value of a data product that can deliver the solution in line with business needs, quality standards and timescales

K15
Knowledge
The engineering principles used (general and software) to investigate and manage the design, development and deployment of new data products within the business

K16
Knowledge
Understand high-performance computer architectures and how to make effective use of these

K17
Knowledge
How to identify current industry trends across ai and data science and how to apply these

K18
Knowledge
The programming languages and techniques applicable to data engineering

K19
Knowledge
The principles and properties behind statistical and machine learning methods

K20
Knowledge
How to collect, store, analyse and visualise data

K21
Knowledge
How ai and data science techniques support and enhance the work of other members of the team

K22
Knowledge
The relationship between mathematical principles and core techniques in ai and data science within the organisational context

K23
Knowledge
The use of different performance and accuracy metrics for model validation in ai projects

K24
Knowledge
Sources of error and bias, including how they may be affected by choice of dataset and methodologies applied

K25
Knowledge
Programming languages and modern machine learning libraries for commercially beneficial scientific analysis and simulation

K26
Knowledge
The scientific method and its application in research and business contexts, including experiment design and hypothesis testing

K27
Knowledge
The engineering principles used (general and software) to create new instruments and applications for data collection

K28
Knowledge
How to communicate concepts and present in a manner appropriate to diverse audiences, adapting communication techniques accordingly

K29
Knowledge
The need for accessibility for all users and diversity of user needs

S1
Skill
Use applied research and data modelling to design and refine the database & storage architectures to deliver secure, stable and scalable data products to the business

S2
Skill
Independently analyse test data, interpret results and evaluate the suitability of proposed solutions, considering current and future business requirements

S3
Skill
Critically evaluate arguments, assumptions, abstract concepts and data (that may be incomplete), to make recommendations and to enable a business solution or range of solutions to be achieved

S4
Skill
Communicate concepts and present in a manner appropriate to diverse audiences, adapting communication techniques accordingly

S5
Skill
Manage expectations and present user research insight, proposed solutions and/or test findings to clients and stakeholders.

S6
Skill
Provide direction and technical guidance for the business with regard to ai and data science opportunities

S7
Skill
Work autonomously and interact effectively within wide, multidisciplinary teams

S8
Skill
Coordinate, negotiate with and manage expectations of diverse stakeholders suppliers with conflicting priorities, interests and timescales

S9
Skill
Manipulate, analyse and visualise complex datasets

S10
Skill
Select datasets and methodologies most appropriate to the business problem

S11
Skill
Apply aspects of advanced maths and statistics relevant to ai and data science that deliver business outcomes

S12
Skill
Consider the associated regulatory, legal, ethical and governance issues when evaluating choices at each stage of the data process

S13
Skill
Identify appropriate resources and architectures for solving a computational problem within the workplace

S14
Skill
Work collaboratively with software engineers to ensure suitable testing and documentation processes are implemented.

S15
Skill
Develop, build and maintain the services and platforms that deliver ai and data science

S16
Skill
Define requirements for, and supervise implementation of, and use data management infrastructure, including enterprise, private and public cloud resources and services

S17
Skill
Consistently implement data curation and data quality controls

S18
Skill
Develop tools that visualise data systems and structures for monitoring and performance

S19
Skill
Use scalable infrastructures, high performance networks, infrastructure and services management and operation to generate effective business solutions.

S20
Skill
Design efficient algorithms for accessing and analysing large amounts of data, including application programming interfaces (api) to different databases and data sets

S21
Skill
Identify and quantify different kinds of uncertainty in the outputs of data collection, experiments and analyses

S22
Skill
Apply scientific methods in a systematic process through experimental design, exploratory data analysis and hypothesis testing to facilitate business decision making

S23
Skill
Disseminate ai and data science practices across departments and in industry, promoting professional development and use of best practice

S24
Skill
Apply research methodology and project management techniques appropriate to the organisation and products

S25
Skill
Select and use programming languages and tools, and follow appropriate software development practices

S26
Skill
Select and apply the most effective/appropriate ai and data science techniques to solve complex business problems

S27
Skill
Analyse information, frame questions and conduct discussions with subject matter experts and assess existing data to scope new ai and data science requirements

S28
Skill
Undertakes independent, impartial decision-making respecting the opinions and views of others in complex, unpredictable and changing circumstances

B1
Behaviour
A strong work ethic and commitment in order to meet the standards required.

B2
Behaviour
Reliable, objective and capable of independent and team working

B3
Behaviour
Acts with integrity with respect to ethical, legal and regulatory ensuring the protection of personal data, safety and security

B4
Behaviour
Initiative and personal responsibility to overcome challenges and take ownership for business solutions

B5
Behaviour
Commitment to continuous professional development; maintaining their knowledge and skills in relation to ai developments that influence their work

B6
Behaviour
Is comfortable and confident interacting with people from technical and non-technical backgrounds. presents data and conclusions in a truthful and appropriate manner

B7
Behaviour
Participates and shares best practice in their organisation, and the wider community around all aspects of ai data science

B8
Behaviour
Maintains awareness of trends and innovations in the subject area, utilising a range of academic literature, online sources, community interaction, conference attendance and other methods which can deliver business value

</competency definitions>
"""

human_writing = """
Revise AI-generated text to read naturally, like something a thoughtful human would write. Focus on clarity, flow, and tone. Apply the following rules:

⸻

1. Punctuation
	•	Avoid em-dashes: Replace with periods or coordinating conjunctions (e.g., “and,” “but”).
	•	Limit semicolons: Only use when mimicking intentional pause or hesitation. Favor shorter, punchier sentences.
	•	Use colons sparingly: Only before clear, necessary lists or to emphasize contrast.
	•	Remove ellipses: Only allow when mimicking natural speech patterns or hesitation in casual dialogue.

⸻

2. Language & Word Choice
	•	Cut hedging phrases: Eliminate or rewrite around “however,” “it’s worth noting,” “in conclusion,” etc. Be direct.
	•	Ditch formality: Replace stiff words like “utilize,” “ascertain,” “therein” with simple alternatives like “use,” “find out,” “there.”
	•	Use contractions in informal writing: Say “don’t” instead of “do not” unless the tone is highly formal.
	•	Rephrase repetitive terms: If a word shows up more than once in close proximity, swap in a synonym or restructure the sentence.

⸻

3. Style & Tone
	•	Vary sentence lengths: Mix short and mid-length sentences. Avoid overly long, complex structures.
	•	Allow minor imperfections: Fragments, unfinished thoughts, or casual transitions are okay in conversational or informal text.
	•	Preserve the core message: Don’t rewrite meaning—just improve delivery.
	•	Match tone to audience: Use formal language for professional settings, relaxed style for casual or friendly writing.
	•	Avoid filler: Cut empty phrases or redundant transitions. Get to the point.

⸻

4. Flow & Readability
	•	Break up dense text: Use paragraph breaks to improve scanability and highlight key ideas.
	•	Highlight key actions or facts: Don’t bury important information under layers of explanation.
	•	Avoid robotic structure: Vary sentence openings. Use natural rhythms.

⸻

Before and After Example
	•	Before:
“The results — though preliminary — suggest success; however, it’s worth noting limitations.”
	•	After:
“The preliminary results suggest success. But there are still some limitations to address.”
"""


st.set_page_config(page_title="Apprenticeship Competencies", page_icon=":material/robot_2:", layout="centered")

st.logo("ac.png", size="large")
st.title(":material/robot_2: Apprenticeship Competencies")


# Simple function to get a response from Groq
@st.cache_resource
def ask_groq(prompt: str, model: str = "meta-llama/llama-4-scout-17b-16e-instruct"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content

st.sidebar.header(":material/settings: Settings")
model = st.sidebar.selectbox("Select a **Model**:", ["moonshotai/kimi-k2-instruct-0905", "meta-llama/llama-4-maverick-17b-128e-instruct", "qwen/qwen3-32b", "openai/gpt-oss-120b"], index=2)
skills = st.sidebar.number_input("Number of Competencies:", min_value=1, max_value=7, value=3)
human = st.sidebar.checkbox("Apply **human writing** style", value=True)
explain = st.sidebar.checkbox("**Explain choices**:", value=True)
activity = st.text_area("**Briefly Describe** what you have Learned:", height=250)

html_content = """<BR><BR><BR><img alt="Static Badge" src="https://img.shields.io/badge/github-janduplessis883-%234a83c0">"""
st.sidebar.html(html_content)


submit = st.button("Generate Competencies", type="primary", icon=":material/next_plan:")
if human and explain:
    prompt = f"I am enrolled in a Data Science Apprenticeship and I need to write competency statements based on what I have learned. Here is a description of what I have learned: {activity}. Using the following list of competencies, write me {skills} competency statements that match what I have learned. Each statement should start with the competency code (e.g., **K1**, **S2**, **B3**) followed by a colon and then the statement. Make sure the statements are clear, concise, and directly related to the activity I described. Here is the list of competencies: {competencies_list}. After you generate the competency statements, please revise them to read naturally, like something a thoughtful human would write. Focus on clarity, flow, and tone. Apply these rules: {human_writing}, after your competency statements write a paragraph explaininig your choices and why you made them, and return the original text for each competency statement."
elif human and not explain:
    prompt = f"I am enrolled in a Data Science Apprenticeship and I need to write competency statements based on what I have learned. Here is a description of what I have learned: {activity}. Using the following list of competencies, write me {skills} competency statements that match what I have learned. Each statement should start with the competency code (e.g., **K1**, **S2**, **B3**) followed by a colon and then the statement. Make sure the statements are clear, concise, and directly related to the activity I described. Here is the list of competencies: {competencies_list}. After you generate the competency statements, please revise them to read naturally, like something a thoughtful human would write. Focus on clarity, flow, and tone. Apply these rules: {human_writing}."
elif not human and explain:
    prompt = f"I am enrolled in a Data Science Apprenticeship and I need to write competency statements based on what I have learned. Here is a description of what I have learned: {activity}. Using the following list of competencies, write me {skills} competency statements that match what I have learned. Each statement should start with the competency code (e.g., **K1**, **S2**, **B3**) followed by a colon and then the statement. Make sure the statements are clear, concise, and directly related to the activity I described. Here is the list of competencies: {competencies_list}, after your competency statements write a paragraph explaininig your choices and why you made them, and return the original text for each competency statement."
elif not human and not explain:
    prompt = f"I am enrolled in a Data Science Apprenticeship and I need to write competency statements based on what I have learned. Here is a description of what I have learned: {activity}. Using the following list of competencies, write me {skills} competency statements that match what I have learned. Each statement should start with the competency code (e.g., **K1**, **S2**, **B3**) followed by a colon and then the statement. Make sure the statements are clear, concise, and directly related to the activity I described. Here is the list of competencies: {competencies_list}."

if submit and activity:
    with st.spinner("Generating competencies...", show_time=True):
        prompt = prompt
        response = ask_groq(prompt, model=model)
        st.write("### Competencies to consider:")
        with st.container(border=True):
            # extract reasoning separately if you still want to make it optional
            match = re.search(r"<think>(.*?)</think>", response, flags=re.DOTALL)
            reasoning = match.group(1).strip() if match else None
            visible_text = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)
            if reasoning:
                with st.expander("Show hidden reasoning", icon=":material/neurology:"):
                    st.markdown(f"{reasoning}")
            st.markdown(visible_text)
            st.toast("Competencies Ready !!", icon=":material/check_circle:", duration=10)
