# The Business of Baseball: Predicting MLB Player Salaries Using Machine Learning

### Background
In Major League Baseball, players receive millions in guaranteed money each season regardless of their performance. MLB teams have begun the process of starting to factor in player performance before dishing out salaries to players. This is still in the beginning stages and a fairly new concept with teams examining the WAR statistic of players. The issue that is created is MLB teams do not know the proper value to pay players. I player can receive a high salary and then underperform or a player could be undervalued and should receive more. This ultimately affects team decisions regarding trades, releasing players, free agents, and acquiring players in the draft. It is possible for MLB teams to better gauge their player needs, payroll distribution, and player salaries by using regression analysis.

### Implementation 
This project uses Gradient Boosting Regression to predict MLB player salaries based on player 
performance. Juypter Notebook was used to gather the salary and player performance data from Fangraphs and Baseball-Reference. It was also used for necessary steps including data exploration, data cleaning, modeling, and evaluating the model. The model was saved and loaded into the baseballapp.py file found in this repository. The repository provides all the necessary files and images for the Streamlit application. To deploy the application, this GitHub repository was connected with Streamlit Cloud. 

### Streamlit Application
The Streamlit application can be accessed by using the link: https://ajp2177-capstone-baseballapp-2ni3m6.streamlit.app/ The application provides the implementation of the Gradient Boosting Regression model to generate predictions based on user input. It also provides features to explore the data used and relevant visualizations. 

To learn more about the project and Streamlit application, check out my presentation. 



![predict page](https://user-images.githubusercontent.com/118642994/221667065-9f504688-bc01-4ad8-a494-b22cb883050d.png)

