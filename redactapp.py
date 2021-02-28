# Core Packages
import streamlit as st 
import os
# import base64

#NLP Pkgs
import spacy
from spacy import displacy
nlp = spacy.load('en')

# # Time Pkg
# import time
# timestr = time.strftime("%Y%m%d-%H%M%S")

#Templates
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

#Function to Redact
def sanitize_names(text):
	docx = nlp(text)
	redacted_sentences = []
	for ent in docx.ents:
		ent.merge()
		for token in docx:
			if token.ent_type_ == 'PERSON':
				redacted_sentences.append(" [REDACTED NAME] ")
			else:
				redacted_sentences.append(token.string)

		return "".join(redacted_sentences)

def sanitize_places(text):
	docx = nlp(text)
	redacted_sentences = []
	for ent in docx.ents:
		ent.merge()
		for token in docx:
			if token.ent_type_ == 'GPE':
				redacted_sentences.append(" [REDACTED PLACES] ")
			else:
				redacted_sentences.append(token.string)

		return "".join(redacted_sentences)

def sanitize_dates(text):
	docx = nlp(text)
	redacted_sentences = []
	for ent in docx.ents:
		ent.merge()
		for token in docx:
			if token.ent_type_ == 'DATE':
				redacted_sentences.append(" [REDACTED PLACES] ")
			else:
				redacted_sentences.append(token.string)

		return "".join(redacted_sentences)

def sanitize_org(text):
	docx = nlp(text)
	redacted_sentences = []
	for ent in docx.ents:
		ent.merge()
		for token in docx:
			if token.ent_type_ == 'ORG':
				redacted_sentences.append(" [REDACTED PLACES] ")
			else:
				redacted_sentences.append(token.string)

		return "".join(redacted_sentences)

#Function Display Entities
# @st.cache
def render_entities(rawtext):
	docx = nlp(rawtext)
	html = displacy.render(docx, style='ent')
	html = html.replace("\n\n","\n")
	result = HTML_WRAPPER.format(html)
	return result

# Function to write to a file
# def writetofile(text,file_name):
# 	with open(os.path.join("downloads",filename),"w") as f:
# 		filename = f.write(text)
# 	return filename


def main():
	st.title("Document Redactor Application")
    # st.text("Built with Streamlit and SpaCy")

	activities = ["Redaction","About"]

	choice = st.sidebar.selectbox("Select Task", activities)

	if choice == "Redaction":
		st.subheader("Redaction of Terms")
		raw_text = st.text_area("Enter Text","Type Here")
		redaction_item = ["names","places","org","dates"]
		redaction_choice = st.selectbox("Select Term to Censor", redaction_item)
		# save_option = st.radio("Save To File", ("Yes", "No"))
		if st.button("Submit"):
			if redaction_choice == 'names':
				result = sanitize_names(raw_text)
			elif redaction_choice == 'places':
				result = sanitize_places(raw_text)
			elif redaction_choice == 'dates':
				result = sanitize_dates(raw_text)
			elif redaction_choice == 'org':
				result = sanitize_org(raw_text)
			st.subheader("Original Text")
			st.write(render_entities(raw_text), unsafe_allow_html = True)
			st.subheader("Redacted Text")
			st.write(result)



	

	# elif choice == "Downloads":
	# 	st.subheader("Download List")

	elif choice == "About":
		st.subheader("About")
		st.text("Major Project - Document Redaction")
		st.text("Usha Mittal Institute of Technology")
		st.text("Guide: Amarpali ")
		st.text("Members: Diksha Verma, Aishwarya Rao, Prachi Rane")


if __name__ == '__main__':
	main()

