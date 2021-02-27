# Major-Project : Redacting sensitive information from documents
                                          FAST & AUTO REDACION TOOL
## Introduction
“I’d like people to get a sense of who I am, yet I want to keep my privacy, too.” – Rosamund Pike

Redaction is the process of removing sensitive information from documents.In many regulated industries, redaction plays a crucial role in making sure that confidential data or sensitive information is not viewed by the wrong people – for example, when sharing documents with a third party that include an individual's personally identifiable information (PII). 

What Information Needs Redacting?

    Social security numbers.
    Driver's license or professional license numbers.
    Protected health information and other medical information.
    Financial documents and files.
    Proprietary information or trade secrets.
    Judiciary records.
    Individuals’ addresses, dates and months of birth, and other personally        
    identifiable information (PII)

Nearly every industry needs redaction in some form to protect important information. However, some, like the legal industry and the government, deal with more sensitive information than others.
Another example is healthcare, which is mandated by HIPAA to protect PHI (Protected Health Information) and is also required to notify affected individuals if their information is exposed—potentially crippling public relations.

One of the major problem with redaction is most of the time context of the document can be lost. For Eg below given image.![image](https://user-images.githubusercontent.com/39613338/109378549-74668e00-78f9-11eb-8ca3-f28f154a51fe.png)

### Handling Different Types of Documents
Redaction takes place across different types of industries, therefore model should be able to cater all types documents. For example phrasing of words in a insurance report compared to in a hospital report will be different. For now we are targetting three separate models, so that the model can redacted using a specific domain. - General, Insurance and legal.


## Plan 
Existing-
Using Optical Character Recognition (OCR) for Redaction

OCR technology allows rules-based search engines to locate and mark sensitive information within digital documents for redaction. The OCR redaction process includes a few steps:

    Automated software analyzes the document for PII (paper and microfilm must be scanned first)
    The service sanitizes the file, removing and redacting marked information
    The document is reproduced in its redacted format and restored with other files in a document management system (DMS) or cloud storage
    
 Proposing-
 1. Auto-redactor using NER 
 2. Manual redaction (User Selection Redaction)
 3. Labeller 


## Project Flow 

## Future Work

## Scope
 
