FROM centos
LABEL owner="Anurag Kumar Singh" \
      version="1.0"
RUN yum  install httpd -y && echo "This is my custom httpd docker image" > /var/www/html/index.html
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
EXPOSE 80
