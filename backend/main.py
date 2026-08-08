"""
main.py
-------
NEXUS-9 Quantum Hypercars — Enterprise Backend with 12 Unique Hypercars.
"""

from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NEXUS-9 Quantum Hypercars API",
    description="Backend powering the NEXUS-9 12-hypercar fleet showroom.",
    version="5.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# FULL 12 HYPERCARS CATALOG
# ---------------------------------------------------------------------------
CARS: List[dict] = [
    {
        "id": "cyber-phantom-x",
        "model": "CYBER PHANTOM X",
        "tagline": "The benchmark quantum EV hyperspeed platform.",
        "engine": "Quad EV Motor",
        "top_speed_kmh": 480,
        "hp": 1950,
        "acceleration_sec": 1.75,
        "range_km": 820,
        "price_mega_credits": 3.20,
        "image_url": "https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Quantum-Vectoring AWD", "Level 5 AI Pilot"],
        "icon": "fa-bolt",
        "icon_color": "--neon-cyan",
        "stock": 12,
    },
    {
        "id": "aero-nebula-gt",
        "model": "AERO NEBULA GT",
        "tagline": "Plasma-hybrid grand tourer built for orbital straights.",
        "engine": "Plasma Hybrid V10",
        "top_speed_kmh": 520,
        "hp": 2100,
        "acceleration_sec": 1.65,
        "range_km": 950,
        "price_mega_credits": 4.80,
        "image_url": "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Active Suspension", "Titanium Monocoque"],
        "icon": "fa-atom",
        "icon_color": "--neon-magenta",
        "stock": 7,
    },
    {
        "id": "titan-quantum-v",
        "model": "TITAN QUANTUM V",
        "tagline": "Tachyon-drive flagship. Physics is a suggestion.",
        "engine": "Tachyon Core Drive",
        "top_speed_kmh": 600,
        "hp": 2600,
        "acceleration_sec": 1.40,
        "range_km": 1100,
        "price_mega_credits": 6.10,
        "image_url": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Plasma Thrust Assist", "Graphene Armor"],
        "icon": "fa-shield-halved",
        "icon_color": "--cyber-yellow",
        "stock": 3,
    },
    {
        "id": "chiron-quantum-ed",
        "model": "CHIRON QUANTUM EDITION",
        "tagline": "Hyper-engineered quad-turbo fusion masterpiece.",
        "engine": "Quad-Turbo Fusion W16",
        "top_speed_kmh": 610,
        "hp": 2700,
        "acceleration_sec": 1.35,
        "range_km": 980,
        "price_mega_credits": 8.50,
        "image_url": "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["3D Printed Exhaust", "Carbon Monocoque"],
        "icon": "fa-crown",
        "icon_color": "--cyber-yellow",
        "stock": 2,
    },
    {
        "id": "aura-spectra-x",
        "model": "AURA SPECTRA X",
        "tagline": "Photonic crystal aerodynamic chassis with dual plasma jets.",
        "engine": "Photon Pulse Core",
        "top_speed_kmh": 580,
        "hp": 2450,
        "acceleration_sec": 1.45,
        "range_km": 1020,
        "price_mega_credits": 7.10,
        "image_url": "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Active Electro Wings", "Holographic HUD"],
        "icon": "fa-sun",
        "icon_color": "--neon-cyan",
        "stock": 4,
    },
    {
        "id": "zenith-quantum-r",
        "model": "ZENITH QUANTUM R",
        "tagline": "Dark matter stealth interceptor designed for hypersonic flight.",
        "engine": "Hyper-Flux Anti-Gravity Drive",
        "top_speed_kmh": 630,
        "hp": 2850,
        "acceleration_sec": 1.28,
        "range_km": 1150,
        "price_mega_credits": 9.20,
        "image_url": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Tachyon Brake Shield", "Diamond Carbon Body"],
        "icon": "fa-gem",
        "icon_color": "--neon-magenta",
        "stock": 1,
    },
    {
        "id": "void-raptor-s",
        "model": "VOID RAPTOR S",
        "tagline": "Fusion-core interceptor for neon backroads.",
        "engine": "Fusion Pulse Core",
        "top_speed_kmh": 550,
        "hp": 2250,
        "acceleration_sec": 1.58,
        "range_km": 890,
        "price_mega_credits": 5.50,
        "image_url": "https://images.unsplash.com/photo-1614200187524-dc4b892acf16?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1614200187524-dc4b892acf16?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Dark Matter Exhaust", "Electro Glass"],
        "icon": "fa-meteor",
        "icon_color": "--neon-magenta",
        "stock": 5,
    },
    {
        "id": "apex-phantom-v12",
        "model": "APEX PHANTOM V12",
        "tagline": "Raw Cyber-Aero force with high-decibel plasma exhaust.",
        "engine": "Hybrid V12 Plasma",
        "top_speed_kmh": 430,
        "hp": 1850,
        "acceleration_sec": 1.90,
        "range_km": 780,
        "price_mega_credits": 3.90,
        "image_url": "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Active Rear Diffuser", "Titanium Tips"],
        "icon": "fa-fire",
        "icon_color": "--cyber-yellow",
        "stock": 4,
    },
    {
        "id": "spectre-hyper-gt",
        "model": "SPECTRE HYPER-GT",
        "tagline": "Stealth dark matter chassis build with winglets.",
        "engine": "Dual Magnet-Jet",
        "top_speed_kmh": 500,
        "hp": 2050,
        "acceleration_sec": 1.68,
        "range_km": 910,
        "price_mega_credits": 5.10,
        "image_url": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Radar Absorbent Paint", "Mag-Lev Brakes"],
        "icon": "fa-gauge-high",
        "icon_color": "--neon-cyan",
        "stock": 2,
    },
    {
        "id": "quantum-stealth-s",
        "model": "QUANTUM STEALTH S",
        "tagline": "Zero-latency neural drive interface.",
        "engine": "Flux Pulse EV",
        "top_speed_kmh": 460,
        "hp": 1780,
        "acceleration_sec": 1.82,
        "range_km": 850,
        "price_mega_credits": 2.90,
        "image_url": "https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Flux Battery Cells", "Neural Telemetry"],
        "icon": "fa-microchip",
        "icon_color": "--neon-magenta",
        "stock": 8,
    },
    {
        "id": "solaris-hyper-drive",
        "model": "SOLARIS HYPER DRIVE",
        "tagline": "Photon-cell battery with unlimited energy regeneration.",
        "engine": "Photon Pulse Motor",
        "top_speed_kmh": 580,
        "hp": 2400,
        "acceleration_sec": 1.48,
        "range_km": 1200,
        "price_mega_credits": 7.20,
        "image_url": "https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Solar Photonic Roof", "Recapture Energy"],
        "icon": "fa-sun",
        "icon_color": "--cyber-yellow",
        "stock": 1,
    },
    {
        "id": "chrono-warp-gt",
        "model": "CHRONO WARP GT",
        "tagline": "Temporal velocity dynamics with adaptive winglets.",
        "engine": "Warp Core EV",
        "top_speed_kmh": 590,
        "hp": 2500,
        "acceleration_sec": 1.42,
        "range_km": 1050,
        "price_mega_credits": 6.80,
        "image_url": "https://images.unsplash.com/photo-1502877338535-766e1452684a?auto=format&fit=crop&w=1200&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1502877338535-766e1452684a?auto=format&fit=crop&w=1200&q=80"
        ],
        "detailed_features": ["Time-Dilation HUD", "Stability Fins"],
        "icon": "fa-clock",
        "icon_color": "--neon-cyan",
        "stock": 3,
    }
]

CARS_BY_ID = {c["id"]: c for c in CARS}

def _car_or_404(car_id: str) -> dict:
    car = CARS_BY_ID.get(car_id)
    if not car:
        raise HTTPException(status_code=404, detail=f"Car '{car_id}' not found")
    return car

@app.get("/api/cars", response_model=List[schemas.Car], tags=["cars"])
def list_cars():
    return CARS

@app.get("/api/cars/{car_id}", response_model=schemas.Car, tags=["cars"])
def get_car(car_id: str):
    return _car_or_404(car_id)

@app.post("/api/orders", response_model=schemas.OrderOut, tags=["orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    car = _car_or_404(order.car_id)

    if order.quantity > car["stock"]:
        raise HTTPException(
            status_code=400,
            detail=f"Only {car['stock']} units of {car['model']} left in stock.",
        )

    unit_price = car["price_mega_credits"]
    total_price = round(unit_price * order.quantity, 2)

    db_order = models.Order(
        customer_name=order.customer_name,
        email=order.email,
        phone=order.phone,
        car_id=car["id"],
        car_model=car["model"],
        quantity=order.quantity,
        unit_price=unit_price,
        total_price=total_price,
        notes=order.notes,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    car["stock"] = max(0, car["stock"] - order.quantity)
    return db_order

@app.get("/api/orders", response_model=List[schemas.OrderOut], tags=["orders"])
def list_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).order_by(models.Order.created_at.desc()).all()

@app.get("/api/admin/stats", tags=["admin"])
def get_admin_stats(db: Session = Depends(get_db)):
    orders = db.query(models.Order).all()
    total_revenue = sum(o.total_price for o in orders)
    return {
        "total_orders": len(orders),
        "total_revenue_mc": round(total_revenue, 2),
        "active_cars_in_catalog": len(CARS),
        "system_status": "OPERATIONAL"
    }

@app.post("/api/contact", response_model=schemas.ContactOut, tags=["contact"])
def create_contact_message(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    """Saves the contact form message to the database."""
    db_contact = models.Contact(
        name=contact.name, 
        email=contact.email, 
        message=contact.message
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@app.get("/api/contact", response_model=List[schemas.ContactOut], tags=["contact"])
def list_contacts(db: Session = Depends(get_db)):
    """Admin endpoint to view all contact messages."""
    return db.query(models.Contact).order_by(models.Contact.created_at.desc()).all()

# --- IMPORTANT: Static Files Mount must be the VERY LAST route! ---
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")