### **`README.md`**

```markdown
# Hugging Face MLOps Summarization

This project demonstrates an MLOps pipeline for text summarization using Hugging Face Transformers, Gradio, and GitHub Actions. The application allows users to input text and receive a summarized version using a pre-trained Hugging Face model. The pipeline is automated using GitHub Actions to sync the application with a Hugging Face Space.

---

## **Features**
- **Text Summarization**: Summarize long text using Hugging Face's `distilbart-cnn-12-6` model.
- **Gradio Interface**: A user-friendly web interface for inputting text and viewing summaries.
- **MLOps Automation**: GitHub Actions workflow to automatically sync the application with Hugging Face Spaces.

---

## **Setup**

### **Prerequisites**
- Python 3.8 or higher
- Git
- A Hugging Face account (for creating a Space and generating an access token)

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/amasresha/huggingface-mlops-summarization.git
   cd huggingface-mlops-summarization
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   or
   make install
   ```

3. Set up Hugging Face secrets in GitHub:
   - Go to your GitHub repository > **Settings > Secrets and variables > Actions**.
   - Add the following secrets:
     - `HF_USERNAME`: Your Hugging Face username.
     - `HF_TOKEN`: Your Hugging Face access token.
     - `HF_SPACE_NAME`: The name of your Hugging Face Space.

---

## **Usage**

### **Running Locally**
1. Start the Gradio app:
   ```bash
   python app.py
    or
    make run
   ```
2. Open the provided URL in your browser to access the text summarization interface.

### **Deploying to Hugging Face Spaces**
- The GitHub Actions workflow (`main.yaml`) automatically syncs the application with your Hugging Face Space whenever changes are pushed to the `main` branch.
- To manually trigger the workflow, go to the **Actions** tab in your GitHub repository and click **Run workflow**.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- [Hugging Face](https://huggingface.co/) for the Transformers library and pre-trained models.
- [Gradio](https://gradio.app/) for the easy-to-use web interface.
- [GitHub Actions](https://github.com/features/actions) for CI/CD automation.


