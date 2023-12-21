{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "External data: Drive, Sheets, and Cloud Storage",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [
        "0ENMqxq25szn"
      ],
      "toc_visible": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "cells": [
    {
      "metadata": {
        "colab_type": "text",
        "id": "7Z2jcRKwUHqV"
      },
      "cell_type": "markdown",
      "source": [
        "This notebook provides recipes for loading and saving data from external sources."
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "eikfzi8ZT_rW"
      },
      "cell_type": "markdown",
      "source": [
        "# Local file system"
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "BaCkyg5CV5jF"
      },
      "cell_type": "markdown",
      "source": [
        "## Uploading files from your local file system\n",
        "\n",
        "`files.upload` returns a dictionary of the files which were uploaded.\n",
        "The dictionary is keyed by the file name, the value is the data which was uploaded."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "vz-jH8T_Uk2c",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "uploaded = files.upload()\n",
        "\n",
        "for fn in uploaded.keys():\n",
        "  print('User uploaded file \"{name}\" with length {length} bytes'.format(\n",
        "      name=fn, length=len(uploaded[fn])))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "hauvGV4hV-Mh"
      },
      "cell_type": "markdown",
      "source": [
        "## Downloading files to your local file system\n",
        "\n",
        "`files.download` will invoke a browser download of the file to the user's local computer.\n"
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "p2E4EKhCWEC5",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "with open('example.txt', 'w') as f:\n",
        "  f.write('some content')\n",
        "\n",
        "files.download('example.txt')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "c2W5A2px3doP"
      },
      "cell_type": "markdown",
      "source": [
        "# Google Drive\n",
        "\n",
        "You can access files in Drive in a number of ways, including:\n",
        "1. Using the [native REST API](https://developers.google.com/drive/v3/web/about-sdk);\n",
        "1. Using a wrapper around the API such as [PyDrive](https://gsuitedevs.github.io/PyDrive/docs/build/html/index.html); or\n",
        "1. Mounting your Google Drive in the runtime's virtual machine.\n",
        "\n",
        "Example of each are below."
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "u22w3BFiOveA"
      },
      "cell_type": "markdown",
      "source": [
        "## Mounting Google Drive locally\n",
        "\n",
        "The example below shows how to mount your Google Drive in your virtual machine using an authorization code, and shows a couple of ways to write & read files there. Once executed, observe the new file (`foo.txt`) is visible in https://drive.google.com/\n",
        "\n",
        "Note this only supports reading and writing files; to programmatically change sharing settings etc use one of the other options below."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "RWSJpsyKqHjH",
        "outputId": "15bd239f-5a6a-447d-dd22-01ee5398b991",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 109
        }
      },
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/gdrive')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Go to this URL in a browser: https://accounts.google.com/o/oauth2/auth?client_id=947318989803-6bn6qk8qdgf4n4g3pfee6491hc0brc4i.apps.googleusercontent.com&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&scope=email%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdocs.test%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.photos.readonly%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fpeopleapi.readonly&response_type=code\n",
            "Enter your authorization code:\n",
            "··········\n",
            "Mounted at /content/gdrive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "XDg9OBaYqRMd",
        "outputId": "5df8b65d-20d2-4956-b8a7-e99d4579d567",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "with open('/content/gdrive/My Drive/foo.txt', 'w') as f:\n",
        "  f.write('Hello Google Drive!')\n",
        "!cat /content/gdrive/My\\ Drive/foo.txt"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hello Google Drive!"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "7taylj9wpsA2"
      },
      "cell_type": "markdown",
      "source": [
        "## PyDrive\n",
        "\n",
        "The example below shows 1) authentication, 2) file upload, and 3) file download. More examples are available in the [PyDrive documentation](https://gsuitedevs.github.io/PyDrive/docs/build/html/index.html)"
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "zU5b6dlRwUQk",
        "outputId": "60570a07-c670-4cd1-abb7-19504ee91e86",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        }
      },
      "cell_type": "code",
      "source": [
        "!pip install -U -q PyDrive\n",
        "\n",
        "from pydrive.auth import GoogleAuth\n",
        "from pydrive.drive import GoogleDrive\n",
        "from google.colab import auth\n",
        "from oauth2client.client import GoogleCredentials\n",
        "\n",
        "# 1. Authenticate and create the PyDrive client.\n",
        "auth.authenticate_user()\n",
        "gauth = GoogleAuth()\n",
        "gauth.credentials = GoogleCredentials.get_application_default()\n",
        "drive = GoogleDrive(gauth)\n",
        "\n",
        "# PyDrive reference:\n",
        "# https://gsuitedevs.github.io/PyDrive/docs/build/html/index.html\n",
        "\n",
        "# 2. Create & upload a file text file.\n",
        "uploaded = drive.CreateFile({'title': 'Sample upload.txt'})\n",
        "uploaded.SetContentString('Sample upload file content')\n",
        "uploaded.Upload()\n",
        "print('Uploaded file with ID {}'.format(uploaded.get('id')))\n",
        "\n",
        "# 3. Load a file by ID and print its contents.\n",
        "downloaded = drive.CreateFile({'id': uploaded.get('id')})\n",
        "print('Downloaded content \"{}\"'.format(downloaded.GetContentString()))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Uploaded file with ID 14vDAdqp7BSCQnoougmgylBexIr2AQx2T\n",
            "Downloaded content \"Sample upload file content\"\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "jRQ5_yMcqJiV"
      },
      "cell_type": "markdown",
      "source": [
        "## Drive REST API\n",
        "\n",
        "The first step is to authenticate."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "r-exJtdG3XwJ",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "from google.colab import auth\n",
        "auth.authenticate_user()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "57uSvdv48bp7"
      },
      "cell_type": "markdown",
      "source": [
        "Now we can construct a Drive API client."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "1aNyFO958V13",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "from googleapiclient.discovery import build\n",
        "drive_service = build('drive', 'v3')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "eDLm7MHQEr2U"
      },
      "cell_type": "markdown",
      "source": [
        "With the client created, we can use any of the functions in the [Google Drive API reference](https://developers.google.com/drive/v3/reference/). Examples follow.\n"
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "bRFyEsdfBxJ9"
      },
      "cell_type": "markdown",
      "source": [
        "## Creating a new Drive file with data from Python"
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "F1-nafvN-NwW",
        "outputId": "4466d27b-edd0-4ef1-8a10-0e180a231af2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        }
      },
      "cell_type": "code",
      "source": [
        "# Create a local file to upload.\n",
        "with open('/tmp/to_upload.txt', 'w') as f:\n",
        "  f.write('my sample file')\n",
        "\n",
        "print('/tmp/to_upload.txt contains:')\n",
        "!cat /tmp/to_upload.txt"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/tmp/to_upload.txt contains:\n",
            "my sample file"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "3Jv6jh6HEpP8",
        "outputId": "cfc1186f-68a1-4620-a18f-99bc6d83e82e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "# Upload the file to Drive. See:\n",
        "#\n",
        "# https://developers.google.com/drive/v3/reference/files/create\n",
        "# https://developers.google.com/drive/v3/web/manage-uploads\n",
        "from googleapiclient.http import MediaFileUpload\n",
        "\n",
        "file_metadata = {\n",
        "  'name': 'Sample file',\n",
        "  'mimeType': 'text/plain'\n",
        "}\n",
        "media = MediaFileUpload('/tmp/to_upload.txt', \n",
        "                        mimetype='text/plain',\n",
        "                        resumable=True)\n",
        "created = drive_service.files().create(body=file_metadata,\n",
        "                                       media_body=media,\n",
        "                                       fields='id').execute()\n",
        "print('File ID: {}'.format(created.get('id')))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "File ID: 1Cw9CqiyU6zbXFD9ViPZu_3yX-sYF4W17\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "j5VyISCKFrqU"
      },
      "cell_type": "markdown",
      "source": [
        "After executing the cell above, a new file named 'Sample file' will appear in your [drive.google.com](https://drive.google.com/) file list. Your file ID will differ since you will have created a new, distinct file from the example above."
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "P3KX0Sm0E2sF"
      },
      "cell_type": "markdown",
      "source": [
        "## Downloading data from a Drive file into Python"
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "KHeruhacFpSU",
        "outputId": "dfe7154f-249c-4344-bd62-a3b294ce02b4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "# Download the file we just uploaded.\n",
        "#\n",
        "# Replace the assignment below with your file ID\n",
        "# to download a different file.\n",
        "#\n",
        "# A file ID looks like: 1uBtlaggVyWshwcyP6kEI-y_W3P8D26sz\n",
        "file_id = 'target_file_id'\n",
        "\n",
        "import io\n",
        "from googleapiclient.http import MediaIoBaseDownload\n",
        "\n",
        "request = drive_service.files().get_media(fileId=file_id)\n",
        "downloaded = io.BytesIO()\n",
        "downloader = MediaIoBaseDownload(downloaded, request)\n",
        "done = False\n",
        "while done is False:\n",
        "  # _ is a placeholder for a progress object that we ignore.\n",
        "  # (Our file is small, so we skip reporting progress.)\n",
        "  _, done = downloader.next_chunk()\n",
        "\n",
        "downloaded.seek(0)\n",
        "print('Downloaded file contents are: {}'.format(downloaded.read()))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Downloaded file contents are: my sample file\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "sOm9PFrT8mGG"
      },
      "cell_type": "markdown",
      "source": [
        "# Google Sheets\n",
        "\n",
        "Our examples below will use the existing open-source [gspread](https://github.com/burnash/gspread) library for interacting with Sheets.\n",
        "\n",
        "First, we'll install the package using `pip`."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "Mwu_sWHv4jEo",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "!pip install --upgrade -q gspread"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "qzi9VsEqzI-o"
      },
      "cell_type": "markdown",
      "source": [
        "Next, we'll import the library, authenticate, and create the interface to sheets."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "6d0xJz3VzLOo",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "from google.colab import auth\n",
        "auth.authenticate_user()\n",
        "\n",
        "import gspread\n",
        "from oauth2client.client import GoogleCredentials\n",
        "\n",
        "gc = gspread.authorize(GoogleCredentials.get_application_default())"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "yjrZQUrt6kKj"
      },
      "cell_type": "markdown",
      "source": [
        "Below is a small set of gspread examples. Additional examples are shown on the [gspread Github page](https://github.com/burnash/gspread#more-examples)."
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "WgXqE02UofZG"
      },
      "cell_type": "markdown",
      "source": [
        "## Creating a new sheet with data from Python"
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "tnnYKhGfzGeP",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "sh = gc.create('A new spreadsheet')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "v9Ia9JVc6Zvk"
      },
      "cell_type": "markdown",
      "source": [
        "After executing the cell above, a new spreadsheet will be shown in your sheets list on [sheets.google.com](http://sheets.google.com/)."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "rkwijiH72BCm",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "# Open our new sheet and add some data.\n",
        "worksheet = gc.open('A new spreadsheet').sheet1\n",
        "\n",
        "cell_list = worksheet.range('A1:C2')\n",
        "\n",
        "import random\n",
        "for cell in cell_list:\n",
        "  cell.value = random.randint(1, 10)\n",
        "\n",
        "worksheet.update_cells(cell_list)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "vRWjiZka9IvT"
      },
      "cell_type": "markdown",
      "source": [
        "After executing the cell above, the sheet will be populated with random numbers in the assigned range."
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "k9q0pp33dckN"
      },
      "cell_type": "markdown",
      "source": [
        "## Downloading data from a sheet into Python as a Pandas DataFrame\n",
        "\n",
        "We'll read back to the data that we inserted above and convert the result into a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).\n",
        "\n",
        "(The data you observe will differ since the contents of each cell is a random number.)"
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "JiJVCmu3dhFa",
        "outputId": "783cdfff-087b-48c4-c1aa-637045b07980",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 126
        }
      },
      "cell_type": "code",
      "source": [
        "# Open our new sheet and read some data.\n",
        "worksheet = gc.open('A new spreadsheet').sheet1\n",
        "\n",
        "# get_all_values gives a list of rows.\n",
        "rows = worksheet.get_all_values()\n",
        "print(rows)\n",
        "\n",
        "# Convert to a DataFrame and render.\n",
        "import pandas as pd\n",
        "pd.DataFrame.from_records(rows)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[['10', '5', '6'], ['9', '6', '2']]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style>\n",
              "    .dataframe thead tr:only-child th {\n",
              "        text-align: right;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: left;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "      <th>1</th>\n",
              "      <th>2</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>10</td>\n",
              "      <td>5</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>9</td>\n",
              "      <td>6</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    0  1  2\n",
              "0  10  5  6\n",
              "1   9  6  2"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 0
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "S7c8WYyQdh5i"
      },
      "cell_type": "markdown",
      "source": [
        "# Google Cloud Storage (GCS)\n",
        "\n",
        "We'll start by authenticating to GCS and creating the service client."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "xM70QWdxeE7q",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "from google.colab import auth\n",
        "auth.authenticate_user()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "NAM6vyXAfVUj"
      },
      "cell_type": "markdown",
      "source": [
        "## Upload a file from Python to a GCS bucket\n",
        "\n",
        "We'll start by creating the sample file to be uploaded."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "LADpx7LReOMk",
        "outputId": "46db7cfa-9ad8-405b-f715-b466a3b2cb7a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        }
      },
      "cell_type": "code",
      "source": [
        "# Create a local file to upload.\n",
        "with open('/tmp/to_upload.txt', 'w') as f:\n",
        "  f.write('my sample file')\n",
        "\n",
        "print('/tmp/to_upload.txt contains:')\n",
        "!cat /tmp/to_upload.txt"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/tmp/to_upload.txt contains:\n",
            "my sample file"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "BCiCo3v9fwch"
      },
      "cell_type": "markdown",
      "source": [
        "Next, we'll upload the file using the `gsutil` command, which is included by default on Colab backends."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "VYC5CyAbAtU7",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "# First, we need to set our project. Replace the assignment below\n",
        "# with your project ID.\n",
        "project_id = 'Your_project_ID_here'"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "TpnuFITI6Tzu",
        "outputId": "04f1dd6d-4d7e-4264-b37b-1e8f645d6d38",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "!gcloud config set project {project_id}"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Updated property [core/project].\r\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "Bcpvh_R_6jKB",
        "outputId": "e1c132b8-6a5c-46db-b1fa-f5768089890c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "import uuid\n",
        "\n",
        "# Make a unique bucket to which we'll upload the file.\n",
        "# (GCS buckets are part of a single global namespace.)\n",
        "bucket_name = 'colab-sample-bucket-' + str(uuid.uuid1())\n",
        "\n",
        "# Full reference: https://cloud.google.com/storage/docs/gsutil/commands/mb\n",
        "!gsutil mb gs://{bucket_name}"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Creating gs://colab-sample-bucket-44971372-baaf-11e7-ae30-0242ac110002/...\r\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "L5cMl7XV65be",
        "outputId": "bb51e51d-7f5f-4e2b-935c-203b8d314115",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 92
        }
      },
      "cell_type": "code",
      "source": [
        "# Copy the file to our new bucket.\n",
        "# Full reference: https://cloud.google.com/storage/docs/gsutil/commands/cp\n",
        "!gsutil cp /tmp/to_upload.txt gs://{bucket_name}/"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Copying file:///tmp/to_upload.txt [Content-Type=text/plain]...\n",
            "/ [1 files][   14.0 B/   14.0 B]                                                \n",
            "Operation completed over 1 objects/14.0 B.                                       \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "pJGU6gX-7M-N",
        "outputId": "38db2bd3-0879-4a2e-8f41-c9495ba570a9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "# Finally, dump the contents of our newly copied file to make sure everything worked.\n",
        "!gsutil cat gs://{bucket_name}/to_upload.txt"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "my sample file"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "0ENMqxq25szn"
      },
      "cell_type": "markdown",
      "source": [
        "### Using Python"
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "YnN-iG9y56V-"
      },
      "cell_type": "markdown",
      "source": [
        "This section demonstrates how to upload files using the native Python API rather than `gsutil`.\n",
        "\n",
        "This snippet is based on [a larger example](https://github.com/GoogleCloudPlatform/storage-file-transfer-json-python/blob/master/chunked_transfer.py) with additional uses of the API."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "YsXBVQqkArHD",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "# The first step is to create a bucket in your cloud project.\n",
        "#\n",
        "# Replace the assignment below with your cloud project ID.\n",
        "#\n",
        "# For details on cloud projects, see:\n",
        "# https://cloud.google.com/resource-manager/docs/creating-managing-projects\n",
        "project_id = 'Your_project_ID_here'"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "YFVbF4cdhd9Y",
        "outputId": "ffa2a4ec-ee02-4fc2-8ed4-a4d73d04e6be",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "# Authenticate to GCS.\n",
        "from google.colab import auth\n",
        "auth.authenticate_user()\n",
        "\n",
        "# Create the service client.\n",
        "from googleapiclient.discovery import build\n",
        "gcs_service = build('storage', 'v1')\n",
        "\n",
        "# Generate a random bucket name to which we'll upload the file.\n",
        "import uuid\n",
        "bucket_name = 'colab-sample-bucket' + str(uuid.uuid1())\n",
        "\n",
        "body = {\n",
        "  'name': bucket_name,\n",
        "  # For a full list of locations, see:\n",
        "  # https://cloud.google.com/storage/docs/bucket-locations\n",
        "  'location': 'us',\n",
        "}\n",
        "gcs_service.buckets().insert(project=project_id, body=body).execute()\n",
        "print('Done')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Done\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "ppkrR7p4mx_P"
      },
      "cell_type": "markdown",
      "source": [
        "The cell below uploads the file to our newly created bucket."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "cFAq-F2af5TJ",
        "outputId": "d07f7059-5767-4d58-ac71-e457a76e8c07",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "from googleapiclient.http import MediaFileUpload\n",
        "\n",
        "media = MediaFileUpload('/tmp/to_upload.txt', \n",
        "                        mimetype='text/plain',\n",
        "                        resumable=True)\n",
        "\n",
        "request = gcs_service.objects().insert(bucket=bucket_name, \n",
        "                                       name='to_upload.txt',\n",
        "                                       media_body=media)\n",
        "\n",
        "response = None\n",
        "while response is None:\n",
        "  # _ is a placeholder for a progress object that we ignore.\n",
        "  # (Our file is small, so we skip reporting progress.)\n",
        "  _, response = request.next_chunk()\n",
        "\n",
        "print('Upload complete')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Upload complete\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "cyqTizOtnZEf"
      },
      "cell_type": "markdown",
      "source": [
        "Once the upload has finished, the data will appear in the cloud console storage browser for your project:\n",
        "\n",
        "https://console.cloud.google.com/storage/browser?project=YOUR_PROJECT_ID_HERE"
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "Q2CWQGIghDux"
      },
      "cell_type": "markdown",
      "source": [
        "## Downloading a file from GCS to Python\n",
        "\n",
        "Next, we'll download the file we just uploaded in the example above. It's as simple as reversing the order in the `gsutil cp` command."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "lPdTf-6O73ll",
        "outputId": "a6da299e-00ff-42a7-f845-9a93a4ccce61",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 110
        }
      },
      "cell_type": "code",
      "source": [
        "# Download the file.\n",
        "!gsutil cp gs://{bucket_name}/to_upload.txt /tmp/gsutil_download.txt\n",
        "  \n",
        "# Print the result to make sure the transfer worked.\n",
        "!cat /tmp/gsutil_download.txt"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Copying gs://colab-sample-bucket483f20dc-baaf-11e7-ae30-0242ac110002/to_upload.txt...\n",
            "/ [1 files][   14.0 B/   14.0 B]                                                \n",
            "Operation completed over 1 objects/14.0 B.                                       \n",
            "my sample file"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "s6nDq8Nk7aPN"
      },
      "cell_type": "markdown",
      "source": [
        "### Using Python"
      ]
    },
    {
      "metadata": {
        "colab_type": "text",
        "id": "P6aWjfTv7bit"
      },
      "cell_type": "markdown",
      "source": [
        "We repeat the download example above using the native Python API."
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "z1_FuDjAozF1",
        "outputId": "ab14cf25-7b51-41c9-d88c-9a94f5c79dfc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        }
      },
      "cell_type": "code",
      "source": [
        "# Authenticate to GCS.\n",
        "from google.colab import auth\n",
        "auth.authenticate_user()\n",
        "\n",
        "# Create the service client.\n",
        "from googleapiclient.discovery import build\n",
        "gcs_service = build('storage', 'v1')\n",
        "\n",
        "from apiclient.http import MediaIoBaseDownload\n",
        "\n",
        "with open('/tmp/downloaded_from_gcs.txt', 'wb') as f:\n",
        "  request = gcs_service.objects().get_media(bucket=bucket_name,\n",
        "                                            object='to_upload.txt')\n",
        "  media = MediaIoBaseDownload(f, request)\n",
        "\n",
        "  done = False\n",
        "  while not done:\n",
        "    # _ is a placeholder for a progress object that we ignore.\n",
        "    # (Our file is small, so we skip reporting progress.)\n",
        "    _, done = media.next_chunk()\n",
        "\n",
        "print('Download complete')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Download complete\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "metadata": {
        "colab_type": "code",
        "id": "DxLyhaiBpAGX",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "# Inspect the file we downloaded to /tmp\n",
        "!cat /tmp/downloaded_from_gcs.txt"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}