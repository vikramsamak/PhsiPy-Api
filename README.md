# PhsiPy-Api

## Rest API for Advanced Scientific Calculations

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
![FastAPI](https://img.shields.io/badge/FastAPI-0.85.1-green.svg)
![Deployed on Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black.svg)

## Overview

**PhsiPy-Api** is a REST API designed to simplify complex scientific calculations. Built using Python and FastAPI, this API provides a wide range of physics-based calculations with high precision and efficiency. The API can be easily integrated into applications that require backend physics computations.

## Features

- **Comprehensive Calculations**: Supports a variety of physics calculations, including mechanics, electromagnetism, thermodynamics, and more.
- **Fast and Scalable**: Built on FastAPI, ensuring high performance and scalability.
- **Easy to Use**: Simple RESTful endpoints designed for quick integration into any application.
- **Deployed on Vercel**: Accessible globally with reliable hosting.
- **Open Source**: Licensed under MIT, making it free to use and contribute.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **FastAPI**
- **Uvicorn**
- **Vercel CLI** (for deployment)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vikramsamak/PhsiPy-Api.git
   cd PhsiPy-Api
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API locally:

   ```bash
   fastapi dev main.py
   ```

   The API will be accessible at `http://127.0.0.1:8000`.

## Documentation

- **In Production**: Access the API documentation at [Production Docs](https://phsipy-api.vercel.app/docs).

- **In Development**: Access the API documentation locally at [Development Docs](http://127.0.0.1:8000/docs).

## Contributing

We welcome contributions from the community. To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Open a pull request.

## Acknowledgements

We would like to express our gratitude to the developers and contributors of **PhysiPy**, a powerful Python library that significantly enhances the capabilities of our API. PhysiPy provides a comprehensive collection of physics formulas and constants, facilitating accurate and efficient calculations across various branches of physics, including mechanics, electromagnetism, thermodynamics, and quantum mechanics.

We extend our special thanks to **Rohan Kishore**, whose contributions and dedication to the development of the PhysiPy library have been instrumental in streamlining our development process. His efforts have enabled users to perform complex calculations without extensive manual coding, making it an invaluable resource for students, researchers, and enthusiasts alike.

For more information about PhysiPy, please visit the official repository: [PhysiPy GitHub Repository](https://github.com/rohankishore/PhysiPy) developed by Rohan Kishore. To learn more about Rohan Kishore, please check his profile at [Rohan Kishore GitHub](https://github.com/rohankishore).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
