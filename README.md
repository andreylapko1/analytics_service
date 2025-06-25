# My Awesome Analytics Project

This project is a Django web application designed for analyzing product data. It allows users to parse product information from a source, view aggregated data, and interact with it via a web interface and a REST API.

---

## Getting Started

Follow these steps to get your project up and running on your local machine.

### Prerequisites

* Python 3.10+
* pip (Python package installer)
* Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/andreylapko1/analytics_service
    cd your_project_folder
    ```
    *(**Note:** Replace `https://github.com/andreylapko1/analytics_service` with the actual URL of your Git repository.)*

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    ```
    * **On Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

3.  **Install required libraries:**
    If you don't have a `requirements.txt` file yet, generate it first:
    ```bash
    pip freeze > requirements.txt
    ```
    Then, install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (optional, for admin panel access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set up your administrator account.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will now be accessible in your web browser at `http://127.0.0.1:8000/`.

---

## Usage

Once the server is running, navigate to `http://127.0.0.1:8000/analys/` (or your project's main URL) in your web browser. From there, you can:

* Enter a **product category** (e.g., "smartphones", "Formula 1").
* Specify the **number of pages** to parse.
* Click "Отправить" (Send) to initiate data parsing and view the results on the dashboard.

---

## API Endpoints

This project also exposes a REST API for programmatic access to product data.

### Product List API

* **Endpoint:** `/api/products/`
* **Method:** `GET`
* **Description:** Retrieves a list of products, potentially filtered or ordered.

#### Filtering Support

The API supports filtering, which can be applied via URL query parameters.

* **Filter by Category Name:** You can filter products by their associated category's name.
    * **Parameter:** `category__name`
    * **Example:** `GET /api/products/?category__name=Electronics`

#### Ordering Support

You can order the results by specific fields by using the `ordering` parameter. Prefix a field name with a hyphen (`-`) for descending order.

* **Parameter:** `ordering`
* **Supported Fields:** `product_price`, `product_rate`, `review_count`
* **Example:** `GET /api/products/?ordering=-product_price` (orders by price in descending order)

---

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository, make your changes, and submit a pull request!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.