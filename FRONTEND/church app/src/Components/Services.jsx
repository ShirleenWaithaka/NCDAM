import React from 'react';
import '../styles/Services.css';

const Services = () => {
  const services = [
    {
      id: 1,
      name: 'Sunday Service',
      time: '9:00 AM - 11:00 AM',
      description: 'Main worship service for all members',
      location: 'Main Sanctuary'
    },
    {
      id: 2,
      name: 'Youth Service',
      time: '2:00 PM - 4:00 PM',
      description: 'Special service for young adults and teens',
      location: 'Youth Hall'
    },
    {
      id: 3,
      name: 'Midweek Services',
      time: 'Every Wednesday, 5:30 PM - 8:00 PM',
      description: 'Mid-week prayer and worship service',
      location: 'Main Sanctuary'
    },
    {
      id: 4,
      name: 'Worship Experience',
      time: 'Every Last Friday, 6:00 PM - 10:00 PM',
      description: 'Monthly worship night and spiritual renewal',
      location: 'Main Sanctuary'
    },
    {
      id: 5,
      name: 'Bible Study',
      time: 'Wednesday, 6:00 PM - 7:30 PM',
      description: 'Mid-week bible study and prayer meeting',
      location: 'Fellowship Hall'
    },
    {
      id: 6,
      name: 'Children\'s Church',
      time: 'Sunday, 9:00 AM - 11:00 AM',
      description: 'Children\'s worship and biblical teachings',
      location: 'Children\'s Wing'
    }
  ];

  return (
    <div className="services-background">
      <div className="services-container">
        <h1 className="services-title">Our Services</h1>
        
        <div className="services-grid">
          {services.map((service) => (
            <div key={service.id} className="service-card">
              <div className="service-content">
                <h2 className="service-name">{service.name}</h2>
                <div className="service-time">
                  <i className="far fa-clock"></i>
                  <span>{service.time}</span>
                </div>
                <div className="service-location">
                  <i className="fas fa-map-marker-alt"></i>
                  <span>{service.location}</span>
                </div>
                <p className="service-description">{service.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Services;