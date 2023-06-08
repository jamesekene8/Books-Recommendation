<a name="readme-top"></a>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<h2>INTRODUCTION</h2>
In this project, I developed a recommender system for self-help books on Amazon. The goal of the project was to scrape data from Amazon, perform exploratory data analysis on the data, store the data in a PostgreSQL database, practice querying the database using SQL commands, and build a recommender system to suggest books based on user input.

<h4>METHODOLOGY</h4>
The project involved the following steps:
<ol>
   <li><strong>Web Scraping</strong>: I scraped data on self-help books from Amazon using Python's Beautiful Soup library. The data collected included book title, author, price, customer ratings, and other relevant information.</li>

  <li><strong>Exploratory Data Analysis (EDA)</strong>: I analyzed the data in the CSV file to understand the distribution of variables, detect outliers, identify trends, and create visualizations. I used Python libraries such as Pandas, NumPy, and Matplotlib to perform EDA.</li>

  <li><strong>Database Management</strong>: I created a PostgreSQL database and a table to store the data I had collected. I used Python's psycopg2 library to write the data from the CSV file to the database.</li>

  <li><strong>SQL Queries</strong>: I practiced querying the database using SQL commands such as SELECT, WHERE, GROUP BY, and JOIN to extract information from the data. I used SQL queries to explore relationships between variables and answer specific questions about the data.</li>

  <li><strong>Recommender System</strong>: I developed a recommender system that takes user input and suggests books based on the data in the PostgreSQL database. I used Python's scikit-learn library to build a collaborative filtering-based recommender system.</strong>

</ol>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Python][Python.com]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

Here are some instructions on how to run this application

### Prerequisites

Here are some things you are going to need to install.

- python: Avalaible at https://www.python.org/downloads/
- PostgreSQL: https://www.postgresql.org/download/
- Pandas
  ```sh
  pip install pandas
  ```
- Seaborn
  ```sh
  pip install seaborn
  ```
- Pandas
  ```sh
  pip install matplotlib
  ```
- Psycopg
  ```sh
  pip install psycopg2
  ```
- BeautifulSoup
  ```sh
  pip install beautifulsoup4
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/jamesekene8/Books-Recommendation
   ```
2. Create your own .env fie in the root directory of your project
   ```js
   DATABASE='your own database name'
   USER='your own database user name
   PASSWORD='your own database password'
   PORT='your own port databse port'
   ```
3. Run the ffg command on the root directory of your project

```sh
python app.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Books-Recommendation`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/Books-Recommendation`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

James Uguna - [@jaeuguna8](https://twitter.com/jaeuguna8) - jamesekene8@gmail.com

Project Link: [https://github.com/jamesekene8/Books-Recommendation](https://github.com/jamesekene8/Books-Recommendation)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Python.com]: https://img.shields.io/badge/Python-Blue?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://jquery.com
