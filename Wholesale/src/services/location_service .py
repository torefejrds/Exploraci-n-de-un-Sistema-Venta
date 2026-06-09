from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session

from datetime import datetime, timezone

from dtos.location.location_create import LocationCreateDTO
from dtos.location.location_update import LocationUpdateDTO
from models.location import Location
from repositories.location_repository import LocationRepository


class LocationService:
    
    @staticmethod
    def get_locations(db: Session):
        return LocationRepository.get_locations(db = db)
    
    @staticmethod
    def find_location(location_id: int, db: Session):
        location = LocationRepository.find_location(location_id = location_id, db = db)
        
        if not location:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Location not found"
            )
        
        return location
    
    @staticmethod
    def create_location(dto: LocationCreateDTO, db: Session):    
        # Create data
        data = Location(
            client_id = dto.client_id,
            name = dto.name,
            address = dto.address,
            city = dto.city,
            state = dto.state,
            postal_code = dto.postal_code,
            phone = dto.phone,
            email = dto.email,
            active = True,
            created_at = datetime.now(timezone.utc),
            updated_at = datetime.now(timezone.utc)
        )
        
        # Return result
        return LocationRepository.create_location(data = data, db = db)
    
    @staticmethod
    def update_location(dto: LocationUpdateDTO, db: Session):
        # Create data
        data = Location(
            id = dto.id,
            client_id = dto.client_id,
            name = dto.name,
            address = dto.address,
            city = dto.city,
            state = dto.state,
            postal_code = dto.postal_code,
            phone = dto.phone,
            email = dto.email,
            updated_at = datetime.now(timezone.utc)
        )
        
        # Update location
        location = LocationRepository.update_location(data = data, db = db)
        
        if not location:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Location not found"
            )
        
        return location
    
    
    @staticmethod
    def delete_location(location_id: int, db: Session):
        location = LocationRepository.delete_location(location_id = location_id, db = db)
            
        if not location:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Location not found"
            )
        
        return location