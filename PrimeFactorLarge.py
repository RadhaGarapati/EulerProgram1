{
    "cells": [
        {
            "cell_type": "code",
            "execution_count": 7,
            "metadata": {},
            "outputs": [
                {"name": "stdout", "output_type": "stream", "text": ["6857\n"]}
            ],
            "source": [
                "def main():\n",
                "    target= 600851475143\n",
                "    potential_factor=2\n",
                "    list_of_prime_factors=[]\n",
                "    while(target>1):\n",
                "        if target % potential_factor==0:\n",
                "            list_of_prime_factors.append(potential_factor)\n",
                "            target= target/potential_factor\n",
                "        else:\n",
                "            potential_factor+=1\n",
                "    print(max(list_of_prime_factors))\n",
                "    \n",
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
