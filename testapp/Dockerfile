# Dockerfile
FROM php:8.4-cli

# Install dependencies including libonig-dev
RUN apt-get update -y && apt-get install -y \
    libonig-dev \
    unzip

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install PHP extensions
RUN docker-php-ext-install pdo mbstring

WORKDIR /app

COPY . /app


RUN composer install



# Install project dependencies

EXPOSE 8000
CMD php -S 0.0.0.0:8000 -t public

