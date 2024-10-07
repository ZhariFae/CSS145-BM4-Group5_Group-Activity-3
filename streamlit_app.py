import streamlit as st
import pandas as pd

st.title("CSS145 Group Activity 3")
st.markdown("### BM4, Group 5")
st.markdown("###### GATMAITAN, Gilbert Jan")
st.markdown("###### PALMA, Gian Carlo")
st.markdown("###### REYES, Jedidiah - ")
st.markdown("###### VILLAFRANCA, Johan Takkis")
st.markdown("###### VIOLENTA, Erielson Emmanuel")

st.markdown("#### Data Upload")
st.code("""
from google.colab import files
uploaded = files.upload()
""")

# Library Imports
st.markdown("#### Library Imports")
st.code("""
import squarify
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
""")

# Dataset Load
st.markdown("#### Dataset Load")
st.code("""
df = pd.read_csv('Electronic_sales_Sep2023-Sep2024.csv')
""")

# Tree Map: Gender
st.markdown("#### Tree Map: Gender")
st.code("""
def treemap_gender():
    gender_counts = df['Gender'].value_counts()
    squarify.plot(gender_counts, label=['Male', 'Female'],  color=['blue', 'pink'])
    plt.axis('off')
    plt.show()

treemap_gender()
""")

st.image("assets/treemap.png", caption="Tree Map: Gender", use_column_width=True)
st.text("The treemap chart compares both genders, showing little difference in product purchases.")

# Line Graph: Ratings
st.markdown("#### Line Graph: Ratings")
st.code("""
def line_chart_ratings():
    rating_counts = df['Rating'].value_counts()
    plt.plot(rating_counts, marker='o', linestyle='-', color='b')
    plt.title('Customer Ratings')
    plt.xlabel('Stars')
    plt.ylabel('No. of Ratings')
    plt.xticks(rotation=45)
    plt.show()

line_chart_ratings()
""")

st.image("assets/linegraph.png", caption="Line Graph: Ratings", use_column_width=True)
st.text("This line graph shows that most customers rated 3 stars, followed by 2 stars.")

# Histogram: Total Price Distribution
st.markdown("#### Histogram: Total Price Distribution")
st.code("""
frequency = df['Total Price']
plt.figure(figsize=(10,10))
plt.hist(frequency, bins=30, color='green')
plt.title('Total Price Distribution')
plt.xlabel('Total Price')
plt.ylabel('Frequency')
plt.show()
""")

st.image("assets/histogram.png", caption="Histogram: Total Price Distribution", use_column_width=True)
st.text("The histogram shows most total prices spent are below 8000.")

# Bubble Chart: Age vs Total Price
st.markdown("#### Bubble Chart: Age vs Total Price")
st.code("""
Age = df['Age']
Total_Price = df['Total Price']
Quantity = df['Quantity']
plt.figure(figsize=(10, 6))
plt.scatter(Age, Total_Price, s=Quantity, alpha=0.5, color='red')
plt.title('Age vs Total Price')
plt.xlabel('Age')
plt.ylabel('Total Price')
""")

st.image("assets/bubblechart.png", caption="Bubble Chart: Age vs Total Price", use_column_width=True)
st.text("The bubble chart shows younger ages spent the most on products.")

# Pie Chart: Payment Preferences
st.markdown("#### Pie Chart: Payment Preferences")
st.code("""
df['Payment Method'] = df['Payment Method'].replace({'Paypal': 'PayPal'})
payment_counts = df['Payment Method'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Payment Preferences Distribution')
plt.show()
""")

st.image("assets/piechart.png", caption="Pie Chart: Payment Preferences", use_column_width=True)
st.text("The pie chart shows Credit Card and PayPal as the most common payment methods.")

# Bar Chart: Product Popularity
st.markdown("#### Bar Chart: Product Popularity")
st.code("""
product_counts = df['Product Type'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(product_counts.index, product_counts.values, color=plt.cm.Paired.colors)
plt.xlabel('Product Type')
plt.ylabel('Number of Purchases')
plt.title('Product Popularity')
plt.xticks(rotation=45)
plt.show()
""")

st.image("assets/barchart.png", caption="Bar Chart: Product Popularity", use_column_width=True)
st.text("The bar chart shows that Smartphones are the most purchased products.")

# Box Chart: Total Price Distribution by Product Type
st.markdown("#### Box Chart: Total Price Distribution by Product Type")
st.code("""
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Product Type', y='Total Price', palette='Set2')
plt.title('Total Price Distribution by Product Type')
plt.xlabel('Product Type')
plt.ylabel('Total Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
""")

st.image("assets/boxchart.png", caption="Box Chart: Total Price Distribution by Product Type", use_column_width=True)
st.text("The box chart shows that Smartphones have the most varied prices.")

# Heatmap: Correlation Heatmap of Customer Data
st.markdown("#### Heatmap: Correlation Heatmap of Customer Data")
st.code("""
numeric_data = df[['Age', 'Rating', 'Total Price']]
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap of Customer Data')
plt.tight_layout()
plt.show()
""")

st.image("assets/heatmap.png", caption="Correlation Heatmap of Customer Data", use_column_width=True)
st.text("The heatmap shows the correlations between Age, Rating, and Total Price.")


# Scatter Plot: Total Price vs Add-on Total
st.markdown("#### Scatter Plot: Total Price vs Add-on Total")
st.code("""
def scatterPlot(df, sample_size=300):
    sample_df = df.sample(n=sample_size, random_state=42)
    price = sample_df['Total Price']
    addon = sample_df['Add-on Total']
    plt.scatter(price, addon, color='green')
    plt.title('Total Price vs. Add-on Total')
    plt.xlabel('Total Price')
    plt.ylabel('Add-on Total')
    plt.grid(True)
    plt.show()

scatterPlot(df, sample_size=200)
""")

st.image("assets/scatterplot.png", caption="Scatter Plot: Total Price vs Add-on Total", use_column_width=True)
st.text("The scatter plot shows a weak positive correlation between Total Price and Add-on Total.")

# Area Map: Total Price over Time
st.markdown("#### Area Map: Total Price over Time")
st.code("""
alt.data_transformers.disable_max_rows()

def areaMap(df, sample_size=500):
    sampled_df = df.sample(n=sample_size, random_state=42)
    area = pd.DataFrame({
        'Purchase Date': pd.to_datetime(sampled_df['Purchase Date']),
        'Total Price': sampled_df['Total Price']
    })
    area_chart = alt.Chart(area).mark_area(opacity=0.5, color='blue').encode(
        x='Purchase Date:T',
        y='Total Price:Q'
    ).properties(
        title='Total Price over Time'
    )
    return area_chart

areaMap(df, sample_size=50).display()
""")

st.image("assets/areamap.png", caption="Area Map: Total Price over Time", use_column_width=True)
st.text("The area map shows the total price of purchases over a 12-month period.")

# Conclusion Section
st.header(" Conclusion")

conclusion_text = """
The data gives us a lot of insight into customer behavior and product trends. When we look at gender, there’s a 
pretty even split between male and female buyers. That might suggest that the products have broad appeal, or it could 
be that the data doesn’t capture other gender identities, so we don’t have a full picture in that respect.

Based on the high ratings (mostly 3, 4, and 5 stars), customers are happy with their purchases. When we look at pricing, 
it shows that most purchases happen at lower price points. It seems the more affordable products attract the majority 
of customers, while fewer people opt for the more expensive items.

Older customers are spending more on average than younger ones. This could be due to older buyers having more financial 
freedom. The data on payment methods shows a clear preference for digital payments, with PayPal and credit cards being 
the most common choices. Cash is still used, but it’s a smaller portion of the payments.

The types of products people buy also reveal trends—smartphones and laptops are the most popular, with accessories and 
other electronics not performing as well. This makes sense, as bigger-ticket items like laptops naturally see higher 
demand. The price differences are also noticeable in the data—laptops tend to be at the higher end, while accessories 
fall on the lower end of the price spectrum.

There’s a slight connection between age and how much people spend. As customers get older, their purchases tend to 
become more expensive. But interestingly, customer satisfaction (as reflected in ratings) stays pretty much the same, 
no matter how much they spend or their age group.

One trend worth noting is that customers who buy more expensive products often also buy add-ons like accessories or 
warranties. This is an opportunity to boost sales by packaging these add-ons with premium products. When we look at how 
sales fluctuate, there are clear peaks—likely tied to specific events, promotions, or seasonal shopping trends. This 
pattern suggests that marketing efforts should focus on these peak times to maximize sales.

Overall, the data provides a clear look into who the customers are, what they’re buying, and how their behavior shifts 
based on factors like age, price, and time of year. These insights can guide strategies for improving sales and customer 
engagement moving forward.
"""
st.write(conclusion_text)
