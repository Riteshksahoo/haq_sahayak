-- SAMPLE APPLICATIONS

INSERT INTO CURATED.CITIZEN_APPLICATIONS
(
    PROCESS_ID,
    DISTRICT_ID,
    APPLICANT_NAME,
    SUBMISSION_DATE,
    STATUS
)
VALUES
(1,1,'Rabindra Kumar Sahoo',CURRENT_DATE(),'Submitted'),
(3,5,'Usha Rani Sahoo',CURRENT_DATE(),'Under Verification'),
(10,8,'Rajesh Kumar Sahoo',CURRENT_DATE(),'Approved');

-- SAMPLE NOTIFICATIONS

INSERT INTO CURATED.NOTIFICATIONS
(
    APPLICATION_ID,
    NOTIFICATION_TYPE,
    MESSAGE
)
VALUES
(101,'STATUS_UPDATE','Your application has been submitted successfully'),
(102,'STATUS_UPDATE','Your application is under verification'),
(103,'STATUS_UPDATE','Your application has been approved');