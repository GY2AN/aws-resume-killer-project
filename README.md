# AWS Resume Killer Project

## Overview
A highly available, secure, and scalable three-tier web application built on AWS.

## Architecture
- VPC with public and private subnets
- Application Load Balancer
- EC2 Auto Scaling Group
- RDS (Multi-AZ)
- CloudFront + S3
- CloudWatch monitoring

```mermaid
flowchart TB

    %% Internet
    Internet((Internet))

    %% VPC Boundary
    subgraph VPC["Custom VPC (10.0.0.0/16)"]

        %% Public Subnets
        subgraph Public["Public Subnets (AZ-a & AZ-b)"]
            ALB[Application Load Balancer]
            NAT[NAT Gateway]
        end

        %% Private Subnets
        subgraph Private["Private Subnets (AZ-a & AZ-b)"]
            
            subgraph ASG["Auto Scaling Group"]
                EC2A[EC2 Instance - Flask App]
                EC2B[EC2 Instance - Flask App]
            end
            
            RDS[(Amazon RDS<br/>Multi-AZ)]
        end

        SSM[SSM Parameter Store]
        CW[CloudWatch Monitoring]

    end

    %% Traffic Flow
    Internet --> ALB
    ALB --> EC2A
    ALB --> EC2B

    %% App to DB
    EC2A --> RDS
    EC2B --> RDS

    %% Outbound Internet Access
    EC2A --> NAT
    EC2B --> NAT
    NAT --> Internet

    %% Secrets Access
    EC2A --> SSM
    EC2B --> SSM

    %% Monitoring
    EC2A --> CW
    EC2B --> CW
    ALB --> CW
```

