{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VnfDHSL-jhQX",
        "outputId": "c6d7f8ac-6855-47e5-8cdf-c3107c48eb4d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install tensorflow\n",
        "!pip install opencv-python\n",
        "!pip install opencv-contrib-python\n",
        "import tensorflow as tf\n",
        "import numpy as np\n",
        "from tensorflow import keras\n",
        "import os\n",
        "import cv2\n",
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator\n",
        "from tensorflow.keras.preprocessing import image"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uwei0k6EjzxD",
        "outputId": "cb49595d-e084-4289-9981-0de67da1c1ec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: tensorflow in /usr/local/lib/python3.7/dist-packages (2.9.2)\n",
            "Requirement already satisfied: wrapt>=1.11.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (1.14.1)\n",
            "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (1.6.3)\n",
            "Requirement already satisfied: flatbuffers<2,>=1.12 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (1.12)\n",
            "Requirement already satisfied: google-pasta>=0.1.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (0.2.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.7/dist-packages (from tensorflow) (57.4.0)\n",
            "Requirement already satisfied: opt-einsum>=2.3.2 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (3.3.0)\n",
            "Requirement already satisfied: keras<2.10.0,>=2.9.0rc0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (2.9.0)\n",
            "Requirement already satisfied: keras-preprocessing>=1.1.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (1.1.2)\n",
            "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (1.50.0)\n",
            "Requirement already satisfied: h5py>=2.9.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (3.1.0)\n",
            "Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (2.1.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.6 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (4.1.1)\n",
            "Requirement already satisfied: numpy>=1.20 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (1.21.6)\n",
            "Requirement already satisfied: gast<=0.4.0,>=0.2.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (0.4.0)\n",
            "Requirement already satisfied: tensorboard<2.10,>=2.9 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (2.9.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from tensorflow) (21.3)\n",
            "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (14.0.6)\n",
            "Requirement already satisfied: protobuf<3.20,>=3.9.2 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (3.17.3)\n",
            "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (0.27.0)\n",
            "Requirement already satisfied: six>=1.12.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (1.15.0)\n",
            "Requirement already satisfied: tensorflow-estimator<2.10.0,>=2.9.0rc0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (2.9.0)\n",
            "Requirement already satisfied: absl-py>=1.0.0 in /usr/local/lib/python3.7/dist-packages (from tensorflow) (1.3.0)\n",
            "Requirement already satisfied: wheel<1.0,>=0.23.0 in /usr/local/lib/python3.7/dist-packages (from astunparse>=1.6.0->tensorflow) (0.38.1)\n",
            "Requirement already satisfied: cached-property in /usr/local/lib/python3.7/dist-packages (from h5py>=2.9.0->tensorflow) (1.5.2)\n",
            "Requirement already satisfied: google-auth<3,>=1.6.3 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.10,>=2.9->tensorflow) (1.35.0)\n",
            "Requirement already satisfied: requests<3,>=2.21.0 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.10,>=2.9->tensorflow) (2.23.0)\n",
            "Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.10,>=2.9->tensorflow) (0.6.1)\n",
            "Requirement already satisfied: werkzeug>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.10,>=2.9->tensorflow) (1.0.1)\n",
            "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.10,>=2.9->tensorflow) (3.4.1)\n",
            "Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.10,>=2.9->tensorflow) (1.8.1)\n",
            "Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in /usr/local/lib/python3.7/dist-packages (from tensorboard<2.10,>=2.9->tensorflow) (0.4.6)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.7/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.10,>=2.9->tensorflow) (0.2.8)\n",
            "Requirement already satisfied: cachetools<5.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.10,>=2.9->tensorflow) (4.2.4)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.7/dist-packages (from google-auth<3,>=1.6.3->tensorboard<2.10,>=2.9->tensorflow) (4.9)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.7/dist-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.10,>=2.9->tensorflow) (1.3.1)\n",
            "Requirement already satisfied: importlib-metadata>=4.4 in /usr/local/lib/python3.7/dist-packages (from markdown>=2.6.8->tensorboard<2.10,>=2.9->tensorflow) (4.13.0)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata>=4.4->markdown>=2.6.8->tensorboard<2.10,>=2.9->tensorflow) (3.10.0)\n",
            "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /usr/local/lib/python3.7/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.10,>=2.9->tensorflow) (0.4.8)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests<3,>=2.21.0->tensorboard<2.10,>=2.9->tensorflow) (1.24.3)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests<3,>=2.21.0->tensorboard<2.10,>=2.9->tensorflow) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests<3,>=2.21.0->tensorboard<2.10,>=2.9->tensorflow) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests<3,>=2.21.0->tensorboard<2.10,>=2.9->tensorflow) (2022.9.24)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.7/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.10,>=2.9->tensorflow) (3.2.2)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->tensorflow) (3.0.9)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: opencv-python in /usr/local/lib/python3.7/dist-packages (4.6.0.66)\n",
            "Requirement already satisfied: numpy>=1.14.5 in /usr/local/lib/python3.7/dist-packages (from opencv-python) (1.21.6)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: opencv-contrib-python in /usr/local/lib/python3.7/dist-packages (4.6.0.66)\n",
            "Requirement already satisfied: numpy>=1.14.5 in /usr/local/lib/python3.7/dist-packages (from opencv-contrib-python) (1.21.6)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train=ImageDataGenerator(rescale=1./255,\n",
        "                                 shear_range=0.2,\n",
        "                                 rotation_range=180,\n",
        "                                 zoom_range=0.2,\n",
        "                                 horizontal_flip=True)\n",
        "train = ImageDataGenerator(rescale=1/255)\n",
        "test = ImageDataGenerator(rescale=1/255)"
      ],
      "metadata": {
        "id": "4mOdBR1BkCOZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_dataset = train.flow_from_directory(\"/content/drive/MyDrive/Dataset/Dataset/train_set\",\n",
        "                                          target_size=(128,128),\n",
        "                                          batch_size = 32,\n",
        "                                          class_mode = 'binary' )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Mv7vksB9kIYK",
        "outputId": "e216fc79-b711-46a0-8ff0-3b8fc39b77e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 436 images belonging to 2 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test_dataset = test.flow_from_directory(\"/content/drive/MyDrive/Dataset/Dataset/test_set\",\n",
        "                                          target_size=(128,128),\n",
        "                                          batch_size = 32,\n",
        "                                          class_mode = 'binary' )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r3gWVNLgkM4F",
        "outputId": "4b24776a-84af-40be-fe9a-f6b772cb1329"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Found 121 images belonging to 2 classes.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "test_dataset.class_indices"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K7kRkC4YkPgl",
        "outputId": "929549b5-fcf8-44e0-d0c2-8ecd415b6ae6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'forest': 0, 'with fire': 1}"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#to define linear initialisation import sequential\n",
        "from keras.models import Sequential\n",
        "#to add layer import Dense\n",
        "from keras.layers import Dense\n",
        "#to create convolution kernel import convolution2D\n",
        "from keras.layers import Convolution2D\n",
        "#import Maxpooling layer\n",
        "from keras.layers import MaxPooling2D\n",
        "#import flatten layer\n",
        "from keras.layers import Flatten\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')"
      ],
      "metadata": {
        "id": "F9eyEUqKkRBR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = keras.Sequential()\n",
        "model.add(Convolution2D(32,(3,3),input_shape=(128,128,3),activation='relu'))\n",
        "model.add(MaxPooling2D(pool_size=(2,2)))\n",
        "model.add(Convolution2D(32,(3,3),activation='relu'))\n",
        "model.add(MaxPooling2D(pool_size=(2,2)))\n",
        "model.add(Convolution2D(32,(3,3),activation='relu'))\n",
        "model.add(MaxPooling2D(pool_size=(2,2)))\n",
        "model.add(Convolution2D(32,(3,3),activation='relu'))\n",
        "model.add(MaxPooling2D(pool_size=(2,2)))\n",
        "model.add(Flatten())"
      ],
      "metadata": {
        "id": "_fy9tvO0kTWo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.add(Dense(150,activation='relu'))\n",
        "\n",
        "model.add(Dense(1,activation='sigmoid'))"
      ],
      "metadata": {
        "id": "SBGnl4iMkVAy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.compile(loss = 'binary_crossentropy',\n",
        "              optimizer = \"adam\",\n",
        "              metrics = [\"accuracy\"])"
      ],
      "metadata": {
        "id": "9S22QmvIkXjo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "r = model.fit(train_dataset, epochs = 5, validation_data = test_dataset)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RD4bBxo-kZUb",
        "outputId": "e2f81de2-5c45-4c76-97fa-f8244101e194"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/5\n",
            "14/14 [==============================] - 92s 7s/step - loss: 0.5798 - accuracy: 0.6628 - val_loss: 0.3330 - val_accuracy: 0.8595\n",
            "Epoch 2/5\n",
            "14/14 [==============================] - 26s 2s/step - loss: 0.4139 - accuracy: 0.8280 - val_loss: 0.1400 - val_accuracy: 0.9504\n",
            "Epoch 3/5\n",
            "14/14 [==============================] - 26s 2s/step - loss: 0.2800 - accuracy: 0.8922 - val_loss: 0.1375 - val_accuracy: 0.9587\n",
            "Epoch 4/5\n",
            "14/14 [==============================] - 27s 2s/step - loss: 0.2440 - accuracy: 0.9014 - val_loss: 0.1224 - val_accuracy: 0.9669\n",
            "Epoch 5/5\n",
            "14/14 [==============================] - 26s 2s/step - loss: 0.1856 - accuracy: 0.9243 - val_loss: 0.0586 - val_accuracy: 0.9752\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "predictions = model.predict(test_dataset)\n",
        "predictions = np.round(predictions)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UTwKaugikbAM",
        "outputId": "61103b72-ae2a-4560-b227-92425bde2a34"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4/4 [==============================] - 5s 1s/step\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "predictions"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ix0ycxeClr1O",
        "outputId": "a8e61ef5-753d-4878-b23a-1e14670dd267"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [1.],\n",
              "       [0.],\n",
              "       [1.],\n",
              "       [0.]], dtype=float32)"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(len(predictions))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bEnOs5ewlvd7",
        "outputId": "f58e5ce5-db13-4b04-c541-0cd7ababdb5e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "121\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model.save(\"/content/drive/MyDrive/archive (1)/forest1.h5\")"
      ],
      "metadata": {
        "id": "6QLmVFqFlx9Q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#import load_model from keras.model\n",
        "from keras.models import load_model\n",
        "#import image class from keras\n",
        "import tensorflow as tf\n",
        "from tensorflow.keras.preprocessing import image\n",
        "#import numpy\n",
        "import numpy as np\n",
        "#import cv2\n",
        "import cv2"
      ],
      "metadata": {
        "id": "Jyc3MylSlztP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = load_model(\"/content/drive/MyDrive/archive (1)/forest1.h5\")"
      ],
      "metadata": {
        "id": "C9eUcTWXmIgP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def predictImage(filename):\n",
        "  img1 = image.load_img(filename,target_size=(128,128))\n",
        "  Y = image.img_to_array(img1)\n",
        "  X = np.expand_dims(Y,axis=0)\n",
        "  val = model.predict(X)\n",
        "  print(val)\n",
        "  if val == 1:\n",
        "    print(\" fire\")\n",
        "  elif val == 0:\n",
        "      print(\"no fire\")"
      ],
      "metadata": {
        "id": "lKU2o8qxmLGO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "predictImage(\"/content/drive/MyDrive/Dataset/Dataset/test_set/with fire/19464620_401.jpg\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9Y4J0xcRmMrO",
        "outputId": "9b6daec0-186c-4208-e9b6-45287fd84d9d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1/1 [==============================] - 0s 125ms/step\n",
            "[[1.]]\n",
            " fire\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install twilio"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L5ro8SE3mO86",
        "outputId": "297e1bec-44cb-49a8-dc53-73b15b46cd30"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting twilio\n",
            "  Downloading twilio-7.15.1-py2.py3-none-any.whl (1.4 MB)\n",
            "\u001b[K     |████████████████████████████████| 1.4 MB 4.9 MB/s \n",
            "\u001b[?25hRequirement already satisfied: requests>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from twilio) (2.23.0)\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.7/dist-packages (from twilio) (2022.6)\n",
            "Collecting PyJWT<3.0.0,>=2.0.0\n",
            "  Downloading PyJWT-2.6.0-py3-none-any.whl (20 kB)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests>=2.0.0->twilio) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests>=2.0.0->twilio) (3.0.4)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests>=2.0.0->twilio) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests>=2.0.0->twilio) (2022.9.24)\n",
            "Installing collected packages: PyJWT, twilio\n",
            "Successfully installed PyJWT-2.6.0 twilio-7.15.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install playsound"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u1GFVreJnKlT",
        "outputId": "d631c790-2ad6-4f4b-96c8-cb09084bddfb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting playsound\n",
            "  Downloading playsound-1.3.0.tar.gz (7.7 kB)\n",
            "Building wheels for collected packages: playsound\n",
            "  Building wheel for playsound (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for playsound: filename=playsound-1.3.0-py3-none-any.whl size=7035 sha256=6cc8a594765dc045811d54129bc5e3fbe95669eecf509234f657cb6a9be4eb0c\n",
            "  Stored in directory: /root/.cache/pip/wheels/ba/f8/bb/ea57c0146b664dca3a0ada4199b0ecb5f9dfcb7b7e22b65ba2\n",
            "Successfully built playsound\n",
            "Installing collected packages: playsound\n",
            "Successfully installed playsound-1.3.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#import opencv librariy\n",
        "import cv2\n",
        "#import numpy\n",
        "import numpy as np\n",
        "#import image function from keras\n",
        "from keras.preprocessing import image\n",
        "#import load_model from keras\n",
        "from keras.models import load_model\n",
        "#import client from twilio API\n",
        "from twilio.rest import Client\n",
        "#imort playsound package\n",
        "from playsound import playsound"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lRYUXaKdnnA_",
        "outputId": "c0e95e37-90e6-4af0-ca72-c65019c4bf19"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:playsound:playsound is relying on another python subprocess. Please use `pip install pygobject` if you want playsound to run more efficiently.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#load the saved model\n",
        "model = load_model(r'/content/drive/MyDrive/archive (1)/forest1.h5')\n",
        "#define video\n",
        "video = cv2.VideoCapture('/content/Fighting Fire with Fire _ Explained in 30 Seconds.mp4')\n",
        "#define the features\n",
        "name = ['forest','with forest']"
      ],
      "metadata": {
        "id": "p6I7mDNen2KO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "account_sid = 'ACde2b15dad8f6e39c32b35eaa64921cf2'\n",
        "auth_token = '1928bb64202abc74a3ff94b70d5deec4'\n",
        "client = Client(account_sid, auth_token)\n",
        "\n",
        "message = client.messages \\\n",
        "    .create(\n",
        "         body='Forest fire is detected , stay alert',\n",
        "         from_='+16075363954',\n",
        "         to='+919488200286'\n",
        "     )\n",
        "\n",
        "print(message.sid)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C0mzy3T6oBUu",
        "outputId": "79041895-7dda-4771-9d49-f39072dd4bcb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "SMcd33e58fa6f60aa349ecba81dce9b48d\n"
          ]
        }
      ]
    }
  ]
}