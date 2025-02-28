import setuptools

setuptools.setup(
    name="df_global_search",
    version="0.1.0",
    author="Carlos D. Serrano",
    author_email="sqlinsights@gmail.com",
    description="Searches for a string in all columns and returns a styled DataFrame if match found. ",
    long_description="This library will create a search grid for your Pandas DataFrame. \n If a match is found, a styled dataframe will be returned with matching columns highlighted.\nSearch can be performed using Text or Regular Expressions.",
    long_description_content_type="text/plain",
    url="https://github.com/sqlinsights/df-global-search",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        "pandas >= 1.5",
        "numpy >= 1.24",
    ],
)
