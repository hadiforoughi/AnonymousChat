<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** hadiforoughi, AnonymousChat, foroughi_hadi, hadiforooghi1377@gmail.com, AnonymousChat, build an anonymous chat with python3
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/hadiforoughi/AnonymousChat">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AnonymousChat</h3>

  <p align="center">
    build an anonymous chat with python3
    <br />
    <a href="https://github.com/hadiforoughi/AnonymousChat/issues">Report Bug</a>
    ·
    <a href="https://github.com/hadiforoughi/AnonymousChat/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is my network course project in which I developed anonymous chat within local networks.In this project client interact with app using CLI. At first, My app sends anonymous chat request to local network via UDP broadcasting, next if anyone accept this request, chat will be started using TCP potocol. The Project description is provided in description.pdf (in persian language).


### Built With

* [python3](https://www.python.org/download/releases/3.0/)



<!-- GETTING STARTED -->
## Getting Started

this project runs on linux operating system, if you don't have linux you must change code for running in your system.

### Prerequisites

* Unix base operating system like [ubuntu 20.04](https://releases.ubuntu.com/20.04/)
* [python3](https://www.python.org/download/releases/3.0/)
* [virtualenv](https://pypi.org/project/virtualenv/)
* [pip3](https://pip.pypa.io/en/stable/)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/hadiforoughi/AnonymousChat.git
   ```
2. create virtualenv


<!-- USAGE EXAMPLES -->
## Usage
after creating virtualenv, cd to working directory and run AnonymousChat.py, you can run this app with below command:
   ```sh
   python3 AnonymousChat.py
   ```
next, app asks your name, enter your name then app show "press 1 for create anonymous chat or 2 for communication" message, if you enter 1 app send request to others client and if anyone accepted, chat will be start or if you press 2 app waiting for request.

![Product Name Screen Shot][product-screenshot]

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/hadiforoughi/AnonymousChat/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Mohammad Hadi Foroughi - [@foroughi_hadi](https://twitter.com/foroughi_hadi) - hadiforooghi1377@gmail.com

Project Link: [https://github.com/hadiforoughi/AnonymousChat](https://github.com/hadiforoughi/AnonymousChat)







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hadiforoughi/AnonymousChat.svg?style=for-the-badge
[contributors-url]: https://github.com/hadiforoughi/license-shield/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hadiforoughi/AnonymousChat.svg?style=for-the-badge
[forks-url]: https://github.com/hadiforoughi/license-shield/network/members
[stars-shield]: https://img.shields.io/github/stars/hadiforoughi/AnonymousChat.svg?style=for-the-badge
[stars-url]: https://github.com/hadiforoughi/license-shield/stargazers
[issues-shield]: https://img.shields.io/github/issues/hadiforoughi/AnonymousChat.svg?style=for-the-badge
[issues-url]: https://github.com/hadiforoughi/license-shield/issues
[license-shield]: https://img.shields.io/github/license/hadiforoughi/AnonymousChat.svg?style=for-the-badge
[license-url]: https://github.com/hadiforoughi/AnonymousChat/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/hadi-foroughi-0130aa169/
[product-screenshot]: images/Screenshot.png
