# finalCapstone 
sentiment_analysis.py
Hyperion Dev Capstone 3 - Sentiment Analysis on Amazon Reviews
The program takes as its input Amazon reviews data (available here https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products).
If you name the csv file 'amazon_product_reviews.csf' and place it in a folder with the program, it will run on that data. If you choose not to do that or would like it to read a different csv file, you are offered the option to enter a file path for that. 
<img width="957" alt="Screenshot 2024-03-02 at 11 18 08" src="https://github.com/aceghlnoorttuy/finalCapstone/assets/152508730/48ede136-46b1-4fc3-a7d0-6b2ee932f39b">
<img width="1008" alt="Screenshot 2024-03-02 at 11 18 24" src="https://github.com/aceghlnoorttuy/finalCapstone/assets/152508730/41259c1f-c5e1-4dd4-b936-1eb6f20a8da9">
The program asks the user what size sample they would like to use and randomly picks the text from that number of reviews. 
<img width="600" alt="Screenshot 2024-03-02 at 11 18 42" src="https://github.com/aceghlnoorttuy/finalCapstone/assets/152508730/591dbb7c-687f-4f0f-a7bf-e231ad75a965">
This text is cleaned and simplified for each, a score is given to assess the positivity of the review, alongside the row number and cleaned text. 
<img width="1236" alt="Screenshot 2024-03-02 at 11 19 17" src="https://github.com/aceghlnoorttuy/finalCapstone/assets/152508730/37cc8b37-bb5f-4f3e-b650-ea542556ea99">
There's also a function to give the similarity of two reviews. Currently, the row numbers are integral to the program, but this can easily be changed to accept user input or generate random rows. 
<img width="344" alt="Screenshot 2024-03-02 at 11 19 36" src="https://github.com/aceghlnoorttuy/finalCapstone/assets/152508730/90e88925-57c4-48e7-a3cc-22ac332b046c">
