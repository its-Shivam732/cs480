# Travel Booking Management System

## Team Members
| **Name**    |                           
|---------------------|
| Shivam Moudgil   smoud3@uic.edu  | 
| Shehriar Burney   sburne4@uic.edu   |  
| Aditya Bagayatkar  abaga@uic.edu|
| Emily Aguilar  emily02@uic.edu|

## Table of Contents

- [Overview](#overview)
  - [Core Features](#core-features)
- [Data Requirements](#data-requirements)
  - [Entities and Relationships](#entities-and-relationships)
- [User Requirements](#user-requirements)
  - [User-Specific Actions](#user-specific-actions)
  - [Admin-Specific Actions](#admin-specific-actions)

---

## Overview
This is a comprehensive platform for managing travel-related operations, including user management, booking travel packages, payment handling, itinerary planning, and reviews. This system aims to streamline the travel process for users and administrators.
The Travel Management System is designed to:
- Allow users to register, book packages, and track rewards.
- Enable administrators to manage users, packages, reviews, and itineraries.
- Provide a seamless travel experience with integrated features.

### Core Features

- **User Management**: User registration, login, profile updates, and rewards tracking.
- **Booking Management**: Booking and track travel packages.
- **Package Management**: View detailed travel packages with destination and itinerary details.
- **Payment Processing**: Secure payment handling and status tracking.
- **Reviews and Ratings**: Submit and view feedback on travel packages.
- **Rewards allocation**: Giving Rewards points to users.
- **Itinerary Planning**: Detailed activity schedules with sub-activities.
- **Administrative Controls**: Manage critical data for smooth operations.

---

## Data Requirements

### Entities and Relationships

#### User
- **Details**: Each user will have first Name, last name , email, password, contact information and boolean attribute is_Admin which shows if given user is admin or not.
- **Relationships**:
  - 1:M with Booking: A user can make multiple bookings.
  - 1:1 with Rewards: A user has one rewards account.
  - 1:M with Review: A user can review multiple packages.

#### Booking
- **Details**: Booking Entity will have booking_id, package_id(associated package), user_id(associated user), Travel dates, booking_date, status details.
- **Relationships**:
  - M:1 with Package: Multiple bookings can be linked to one package.
  - M:1 with User: Multiple booking can be linked to one user.
  - 1:1 with Payment: Each booking has a corresponding payment.

#### Package
- **Details**: This will contain details about package like name, Travel package descriptions, pricing, duration and destination.
- **Relationships**:
  - M:1 with Destination: Multiple packages can belong to one destination.
  - 1:M with Itinerary: A package can have multiple itineraries.
  - 1:M with Review: One Package can have multiple user reviews.

#### Payment
- **Details**: It contains details about booking payment like payment_date, Amount, method, status and booking id associated with it.
- **Relationship**:
  - 1:1 with Booking: Each payment is linked to one booking.

#### Destination
- **Details**: Location details such as city, state, country and location description.
- **Relationship**:
  - 1:M with Package: A destination can host multiple packages.

#### Itinerary
- **Details**: This contains fields like activity name, activity description, package id and parent id which refers to another Itinerary value(sub-activity).
- **Relationships**:
  - 1:M with Package: An itinerary belongs to a specific package.
  - Recursive (1:M): Itinerary entries can have sub-activities.

#### Review
- **Details**: It contains Ratings and reviews for particular user and package.
- **Relationships**:
  - Described in Package and User entries above.

#### Rewards
- **Details**: Contains Rewards points, last updated date associated with user.
- **Relationship**:
  - Described in User entry above.

---

## Application Requirements

### User-Specific Functions

#### General User Actions
- Register and log in to the platform.
- Manage personal profiles, user can edit its own user details.

#### Booking Actions
- Browse and book travel packages. User can browse various travel package and can book any package from the list.
  
#### Itinerary Exploration
- User can view detailed itineraries, including sub-activities associated with each package.

#### Payment Actions
- After booking user can complete secure payments for bookings. User can also see the payment status (eg Success/Failed)

#### Review Actions
- User can submit and view reviews for travel packages.

#### Rewards Actions
- After user succesfully books a package, predifined reward points are automatically added to its account which it can redeem in next booking.

### Admin-Specific Functions

- Manage user accounts (add, update, or deactivate).
- Create, update, and delete travel packages and destinations.
- Moderate and manage reviews.
- Update itineraries with new activities or modifications.

---
