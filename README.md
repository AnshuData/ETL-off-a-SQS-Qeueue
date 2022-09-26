Application that  reads data from an AWS SQS Qeueue, transform that data, then write to a AWS MySQL database

Following steps are implemented to create such end-to-end ETL pipeline:
        a. Creates SQS queue
        b. Send data to AWS SQS queue
        c. Recieve data from SQS queue
        d. Mask user sensitive fields in the data recieved from SQS
        e. Populate AWS MySQL table with such data
