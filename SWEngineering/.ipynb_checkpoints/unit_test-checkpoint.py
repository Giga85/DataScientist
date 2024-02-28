{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bf372862",
   "metadata": {},
   "outputs": [],
   "source": [
    "def days_until_launch(current_day, launch_day):\n",
    "    \"\"\"\"Returns the days left before launch.\n",
    "    \n",
    "    current_day (int) - current day in integer\n",
    "    launch_day (int) - launch day in integer\n",
    "    \"\"\"\n",
    "    if(launch_day < current_day):\n",
    "        return 0\n",
    "    return launch_day - current_day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71a72f5d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
