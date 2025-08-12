📄 EDA Report: Titanic Gender Submission Dataset
📁 Dataset Overview
- File: gender_submission.csv
- Columns:
- PassengerId: Unique identifier for each passenger
- Survived: Binary indicator (0 = did not survive, 1 = survived)
📊 1. Data Info
df.info()


- Total entries: 418
- No missing values
- Data types:
- PassengerId: int64
- Survived: int64

📈 2. Value Counts
df['PassengerId'].value_counts()


- Each PassengerId is unique — confirms it's an identifier, not a feature for modeling.

🔥 3. Correlation Matrix
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')


| Feature | Survived | 
| PassengerId | ~0.006 | 


- Observation: Very weak correlation between PassengerId and Survived, as expected.

🔍 4. Pairplot
sns.pairplot(df)


- With only two numerical columns, the pairplot is minimal.
- Observation: No visible relationship between PassengerId and Survived.

📊 5. Histogram of PassengerId
df['PassengerId'].hist(bins=30)


- Observation: Uniform distribution — IDs are evenly spaced, confirming it's not a feature.

📦 6. Boxplot of Survived
sns.boxplot(x=df['Survived'])


- Observation: Binary distribution (0 and 1 only).
- No outliers or spread — confirms it's a categorical target variable.

🎯 7. Scatterplot: PassengerId vs Survived
sns.scatterplot(x='PassengerId', y='Survived', data=df)


- Observation: Horizontal bands at y = 0 and y = 1.
- No meaningful trend — reinforces that PassengerId is not predictive.

🧾 Summary of Findings
- The dataset contains only two columns: PassengerId and Survived.
- PassengerId is a unique identifier and not useful for modeling or analysis.
- Survived is a binary target variable.
- No correlation or trends exist between the two columns.
- Visualizations confirm the lack of relationships or patterns.


