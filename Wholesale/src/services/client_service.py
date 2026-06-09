from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session

from datetime import datetime, timezone

from dtos.client.client_create import ClientCreateDTO
from dtos.client.client_update import ClientUpdateDTO
from models.client import Client
from repositories.client_repository import ClientRepository

class ClientService:
    
    @staticmethod
    def get_clients(db: Session):
        return ClientRepository.get_clients(db = db)
    
    @staticmethod
    def find_client(client_id: int, db: Session):
        client = ClientRepository.find_client(client_id = client_id, db = db)
        
        if not client:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Client not found"
            )
        
        return client
    
    @staticmethod
    def create_client(dto: ClientCreateDTO, db: Session):                
        # Create data
        data = Client(
            name = dto.name,
            phone = dto.phone,
            email = dto.email,
            rfc = dto.rfc,
            active = True,
            created_at = datetime.now(timezone.utc),
            updated_at = datetime.now(timezone.utc)
        )
        
        # Return result
        return ClientRepository.create_client(data = data, db = db)
    
    @staticmethod
    def update_client(dto: ClientUpdateDTO, db: Session):
        # Create data
        data = Client(
            id = dto.id,
            name = dto.name,
            phone = dto.phone,
            email = dto.email,
            rfc = dto.rfc,
            updated_at = datetime.now(timezone.utc)
        )
        
        # Update client
        client = ClientRepository.update_client(data = data, db = db)
        
        if not client:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Client not found"
            )
        
        return client
    
    
    @staticmethod
    def delete_client(client_id: int, db: Session):
        client = ClientRepository.delete_client(client_id = client_id, db = db)
            
        if not client:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Client not found"
            )
        
        return client