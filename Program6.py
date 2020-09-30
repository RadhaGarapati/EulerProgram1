{
    "cells": [
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [
                {"name": "stdout", "output_type": "stream", "text": ["25164150\n"]}
            ],
            "source": [
                "SumofSquares = 0\n",
                "for i in range(1, 101):\n",
                "    SumofSquares += i * i\n",
                "SquareofSums = 0\n",
                "for i in range(1, 101):\n",
                "    SquareofSums += i\n",
                "SquareofSums = SquareofSums * SquareofSums\n",
                "print(SquareofSums - SumofSquares)\n",
                "\n",
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
