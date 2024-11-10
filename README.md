# Travel Booking Management System

A comprehensive platform for managing travel-related operations, including user management, booking travel packages, payment handling, itinerary planning, and reviews. This system aims to streamline the travel process for users and administrators.

## Team Members
| **Name**    |                           
|---------------------|
| Shivam Moudgil     | 
| Shehriar Burney     |  
| Aditya Bagayatkar |
| Emily Aguilar|

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
- **Details**: Name, email, password, contact information, and registration date.
- **Relationships**:
  - 1:M with Booking: A user can make multiple bookings.
  - 1:1 with Rewards: A user has one rewards account.
  - M:M with Review: A user can review multiple packages.

#### Booking
- **Details**: Travel dates, status, and associated package details.
- **Relationships**:
  - M:1 with Package: A booking is linked to one package.
  - 1:1 with Payment: Each booking has a corresponding payment.

#### Package
- **Details**: Travel package descriptions, pricing, and durations.
- **Relationships**:
  - M:1 with Destination: Multiple packages can belong to one destination.
  - 1:M with Itinerary: A package can have multiple itineraries.
  - M:M with Review: Packages can have multiple user reviews.

#### Payment
- **Details**: Amount, method, and status.
- **Relationship**:
  - 1:1 with Booking: Each payment is linked to one booking.

#### Destination
- **Details**: Location details such as city, state, and country.
- **Relationship**:
  - 1:M with Package: A destination can host multiple packages.

#### Itinerary
- **Details**: Activities planned for each package.
- **Relationships**:
  - 1:M with Package: An itinerary belongs to a specific package.
  - Recursive (1:M): Itinerary entries can have sub-activities.

#### Review
- **Details**: Ratings and review texts for packages.
- **Relationships**:
  - M:M with User and Package: Connects users and packages through reviews.

#### Rewards
- **Details**: Rewards points and last updated date.
- **Relationship**:
  - 1:1 with User: One rewards record per user.

---

## User Requirements

### User-Specific Actions

#### General User Actions
- Register and log in to the platform.
- Manage personal profiles, including preferences and contact details.

#### Booking Actions
- Browse and book travel packages.
- Track booking status and details.

#### Payment Actions
- Complete secure payments for bookings.
- Monitor payment status (e.g., Success, Failed).

#### Review Actions
- Submit and view reviews for travel packages.

#### Rewards Actions
- Track rewards points and redeem them.

#### Itinerary Exploration
- View detailed itineraries, including sub-activities.

### Admin-Specific Actions

- Manage user accounts (add, update, or deactivate).
- Create, update, and delete travel packages and destinations.
- Moderate and manage reviews.
- Update itineraries with new activities or modifications.

---

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/travel-management-system.git
   cd travel-management-system
