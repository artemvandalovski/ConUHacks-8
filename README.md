# Environment Creation

Create the python environment, `conuhacks`, as follows:
```console
conda create --name conuhacks python=3.11
```

Activate the environment as follows:
```console
conda activate conuhacks
```

From the root folder of the project, install the packages required, listed in `requirements.txt`:
```console
pip install -r requirements.txt
```

# Environment Variables

When cloning this project, create an `project_config.json` file to store your configuration. The file contains secret information, such as credentials, and should have the following format:

```json
{
    "database":
    {
        "dbname": "my_database",
        "user": "postgres",
        "password": "password",
        "host": "localhost",
        "port": 5432
    }
}
```

# Project Structure

