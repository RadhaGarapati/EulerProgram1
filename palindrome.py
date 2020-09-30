{
    "cells": [
        {
            "cell_type": "code",
            "execution_count": 9,
            "metadata": {},
            "outputs": [
                {"name": "stdout", "output_type": "stream", "text": ["906609\n"]}
            ],
            "source": [
                "def main():\n",
                "    list_of_palindrome = []\n",
                "    for x in range(100,1000):\n",
                "        for y in range(100,1000):\n",
                "            if str(x*y)== str(x*y)[::-1]:\n",
                "                list_of_palindrome.append(int(x*y))\n",
                "    print(max(list_of_palindrome))\n",
                "main()",
            ],
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [],
        },
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.7.6",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 4,
}
