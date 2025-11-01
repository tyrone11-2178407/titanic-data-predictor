# Step 1: Use Rocker image that already has tidyverse installed
FROM rocker/tidyverse:4.3.2

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy your R scripts and data
COPY src/r/install_package.R .
COPY src/r/titanic_model.R .
COPY src/data ./src/data

# Step 4: Install any extra packages you need
RUN Rscript install_package.R

# Step 5: Run your model
CMD ["Rscript", "titanic_model.R"]
