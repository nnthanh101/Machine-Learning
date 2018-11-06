# Machine Learning by Examples

Machine Learning by Examples using Scikit-Learn, Keras, TensorFlow, PyTorch, and OpenCV.

> 1. [Google Colab Notebooks](colab.research.google.com) (Free Tesla K80 GPU)
> 2. Disease-Prediction using Machine Learning (Scikit-Learn)
> 3. Recruitment Matching using Machine Learning (Keras & Tesorflow)

## 1. Configuring Development Environment using [Google Colab Notebooks](colab.research.google.com)

- [x] 1.1. [Creating Folder on Google Drive](drive.google.com) or choose the default `Colab Notebooks` folder
- [x] 1.2. Opening or Creating a `Colab Notebook
  - [x] Openning 
  - [x] Google Drive: upload [](https://github.com/vbosstech/disease-diagnostic-from-symptoms/archive/master.zip) onto `My Drive/machine-learning`
  - `Google Drive`: `My Drive/machine-learning/disease-diagnostic-from-symptoms/disease_symptoms_data_analysis_DecisionTree.ipynb` > *Open with* > *Colaboratory* 
  - [x] Creating new *Colab Notebook* via *Right click > More > Colaboratory*
- [x] 1.3. Setting Free GPU: 
  - [x] [Google Colab](colab.research.google.com): Edit > Notebook settings: 
    - [x] Runtime type: `Python 3` 
    - [x] Hardware accelerator: `GPU`
- [x] 1.4. Running or Importing Files with Google Colab
     ```
         from google.colab import drive
         drive.mount("/content/gdrive", force_remount=True)
     ```
     Note: Click the link, copy verification code and paste it to text box; then we can use `/content/gdrive/My Drive/`
- [x] 1.5. Install Python Module/Package
     ```
         # Install Excel/GoogleSheet Python module
         !pip3 install --upgrade -q gspread
         !pip3 install --upgrade -q xlrd
         
         # Install Keras
         !pip3 install -q keras
         !pip3 install torch torchvision
     ```
- [x] Google Colab Notebooks
     ```
         # RAM & CPU
         !cat /proc/meminfo
         !cat /proc/cpuinfo
         # Restart Google Colab
         !kill -9 -1
     ```

## 2. Disease-Prediction using Machine Learning (Scikit-Learn)


## 3. Recruitment Matching using Machine Learning (Keras & Tesorflow)

