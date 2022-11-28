    CREATE TABLE Patient_556(
        Address varchar(50) not null,
        DOB date not null,
        Patient_ID varchar(10) not null,
        First_Name varchar(20) not null,
        Last_Name varchar(20) not null,
        Gender varchar(1) not null,
        Email varchar(50) not null,
        Phone bigint(10) not null,
        Primary key(Patient_ID)
    );

    CREATE TABLE Doctor_556(
        Doctor_ID varchar(10) not null,
        Job_type varchar(20) not null,
        First_Name varchar(20) not null,
        Last_Name varchar(20) not null,
        Street varchar(50) not null,
        Pincode int(6) not null,
        Annual_salary int(10) not null,
        Primary key (Doctor_ID)
    );

    CREATE TABLE Appointment_556(
        Appointment_type varchar(40) not null,
        Date_of_Appointment date not null,
        Patient_ID varchar(10) not null,
        End_time varchar(40) not null,
        Appointment_ID varchar(10) not null,
        Start_time varchar(40) not null,
        Doctor_ID varchar(10) not null,
        Primary key (Appointment_ID),
        Foreign key (Patient_ID) references Patient_556
    (Patient_ID),
        Foreign key (Doctor_ID) references Doctor_556
    (Doctor_ID)
    );

    CREATE TABLE Treatment_556(
        Treatment_ID varchar(10) not null,
        Tooth int(4) not null,
        Medication varchar(50),
        Patient_ID varchar(10) not null,
        Appointment_ID varchar(10) not null,
        Doctor_ID varchar(10) not null,
        Primary key (Treatment_ID),
        Foreign key (Patient_ID) references Patient_556
    (Patient_ID),
        Foreign key (Appointment_ID) references Appointment_556
    (Appointment_ID),
        Foreign key (Doctor_ID) references Doctor_556
    (Doctor_ID)
    );

    CREATE TABLE Review_556(
        Treatment_description varchar(100) not null,
        Date_of_review date not null,
        Cleanliness int(2) not null,
        Communication int(2) not null,
        Professionalism int(2) not null,
        Review_ID varchar(7) not null,
        Treatment_ID varchar(10) not null,
        Doctor_ID varchar(10) not null,
        Primary key (Review_ID),
        Foreign key (Treatment_ID) references Treatment_556
    (Treatment_ID),
        Foreign key (Doctor_ID) references Doctor_556
    (Doctor_ID)
    );

    CREATE TABLE Billing_556(
        Bill_ID varchar(10) not null,
        Total_amount int(10) not null,
        Payment_Type varchar(10) not null,
        Patient_ID varchar(10) not null,
        Payment_Status varchar(10) not null,
        Primary key (Bill_ID),
        Foreign key (Patient_ID) references Patient_556
    (Patient_ID)
    );
