<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![pipeline status](https://gitlab.com/sophiabrandt/flask-tdd-docker/badges/master/pipeline.svg)](https://gitlab.com/sophiabrandt/flask-tdd-docker/commits/master)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/sophiabrandt/flask-tdd-docker">
    <img src="logo.png" alt="Logo">
  </a>

  <h3 align="center">Flask TDD Docker</h3>

  <p align="center">
    Developing a Flask REST API with a React front-end - with TDD
    <br />
    <a href="https://github.com/sophiabrandt/flask-tdd-docker"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/sophiabrandt/flask-tdd-docker">View Demo</a>
    ·
    <a href="https://github.com/sophiabrandt/flask-tdd-docker/issues">Report Bug</a>
    ·
    <a href="https://github.com/sophiabrandt/flask-tdd-docker/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

The repo represents my learning progress with the [testdriven.io courses][testdriven] with Flask, Docker and React.


### Built With

* Flask
* Flask-RESTful
* Docker
* React



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

- Docker 19.03.4
- docker-compose 1.25.0

### Installation
 
1. Get the flask-tdd-docker repository
    ```sh
    npx degit https://github.com/sophiabrandt/flask-tdd-docker.git flask-tdd-docker
    ```
2. Build docker containers
    ```sh
    docker-compose build
    ```
3. Run docker containers
    ```sh
    docker-compose up -d
    ```

<!-- USAGE EXAMPLES -->
## Usage

- Run tests:
    ```sh
    docker-compose exec users pytest "project/tests"
    ```

- Recreate database:
    ```sh
    docker-compose exec users python manage.py recreate_db
    ```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/sophiabrandt/flask-tdd-docker/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


**Please note that this is a learning repository, not a real project.**

<!-- LICENSE -->
## License

Code is &copy; Michael Herman 2019, with minor modifications by Sophia Brandt.



<!-- CONTACT -->
## Contact

Sophia Brandt - [@hisophiabrandt](https://twitter.com/hisophiabrandt)

Project Link: [https://github.com/sophiabrandt/flask-tdd-docker](https://github.com/sophiabrandt/flask-tdd-docker)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Michael Herman][testdriven]
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/sophiabrandt/flask-tdd-docker.svg?style=flat-square
[contributors-url]: https://github.com/sophiabrandt/flask-tdd-docker/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/sophiabrandt/flask-tdd-docker.svg?style=flat-square
[issues-url]: https://github.com/sophiabrandt/flask-tdd-docker/issues
[license-shield]: https://img.shields.io/github/license/sophiabrandt/flask-tdd-docker.svg?style=flat-square
[testdriven]: https://testdriven.io/
