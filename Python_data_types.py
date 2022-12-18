{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOMVn0zWEGrno7n3ry7tTcn",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/iamsoankit/Google-Colab/blob/main/Python_data_types.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "au4LM_Vk_2cZ"
      },
      "outputs": [],
      "source": [
        "Python Data Types "
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "```\n",
        "#Integer and Long                 #Sets\n",
        "#Float/Floating Point             #Mappings\n",
        "#Complex Numbers\n",
        "#Boolean::\n",
        "#None\n",
        "#Sequence\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "x3RFdrtgAGn8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "rating = 3.5 #floating\n",
        "print(rating, type(rating) )\n",
        "\n",
        "name = \"Ankit\" #string\n",
        "print(name,type(name))\n",
        "\n",
        "marks = 89\n",
        "print(marks,type (marks))\n",
        "\n",
        "is_passed = True\n",
        "print(is_passed,type(is_passed))\n",
        "\n",
        "complex_number = 5 + 6j #complexnumber\n",
        "print(complex_number,type(complex_number))\n",
        "\n",
        "vegetables_list = ['Brinjal','Tomato','Peas'] #list_datatype\n",
        "print(vegetables_list,type(vegetables_list))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "21_0U9ReA3IK",
        "outputId": "459d941f-745d-444b-eb51-6cbcaaa63f08"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.5 <class 'float'>\n",
            "Ankit <class 'str'>\n",
            "89 <class 'int'>\n",
            "True <class 'bool'>\n",
            "(5+6j) <class 'complex'>\n",
            "['Brinjal', 'Tomato', 'Peas'] <class 'list'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Write a program to save the following values of a user\n",
        "#-Name\n",
        "#-Age\n",
        "#-Year of birth\n",
        "#-Is New User?\n",
        "#-List of his/her favourite food\n",
        "\n"
      ],
      "metadata": {
        "id": "lSZATwUaEPl8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        " name = \"Ankit\"\n",
        " age = 19\n",
        " yearofbirth=2003\n",
        " New_user= True\n",
        " Favourite_food=['Tomato','Peas']\n",
        "\n",
        " print(name)\n",
        " print(age)\n",
        " print(yearofbirth)\n",
        " print(New_user)\n",
        " print(Favourite_food)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LQPF8TsDE0y6",
        "outputId": "f1c2463f-8c94-460a-bdc5-458233460539"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ankit\n",
            "19\n",
            "2003\n",
            "True\n",
            "['Tomato', 'Peas']\n"
          ]
        }
      ]
    }
  ]
}