# Pydantic: Data Validation Library

Why Pydantic is so important in agent engineering: it brings type safety, reliability, and the structure of software engineering to the traditionally unstructured and unpredictable world of LLMs.

## Field Validation: Checking One Field

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class PatientData(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value


    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully to the database!")


patient_data = {"name": "bappy", "email": "bappy@hdfc.com",
                "linkedin_url": "https://www.linkedin.com/in/boktiarahmed73/",
                "age": "25", "weight": 70.5,
                "married": "True",
                "allergies": ["peanuts", "shellfish"],
                "contact_details": {"phone": "123-456-7890"}}

patient_1 = PatientData(**patient_data)

add_patient_data(patient_1)
```

## Model Validation: Checking the Whole Object After All Fields Are Combined

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class PatientData(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully to the database!")


patient_data = {"name": "bappy", "email": "bappy@hdfc.com",
                "linkedin_url": "https://www.linkedin.com/in/boktiarahmed73/",
                "age": "70", "weight": 70.5,
                "married": "True",
                "allergies": ["peanuts", "shellfish"],
                "contact_details": {"phone": "123-456-7890", "emergency": "987-654-3210"}}

patient_1 = PatientData(**patient_data)

add_patient_data(patient_1)
```

**Notes on `mode`:**
- `mode='after'` (used here) runs after all individual fields have already been validated and converted into the model. That's why the parameter is called `model` — it's the fully-built object, so you access fields normally: `model.age`, `model.contact_details`.
- `mode='before'` runs before field validation, while the data is still raw (usually a dict). You'd access it like `data['age']` instead.

## Computed Fields

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class PatientData(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("BMI:", patient.bmi)
    print("Data added successfully to the database!")


patient_data = {"name": "bappy", "email": "bappy@hdfc.com",
                "linkedin_url": "https://www.linkedin.com/in/boktiarahmed73/",
                "age": "70", "weight": 70.5,
                "height": 1.75,
                "married": "True",
                "allergies": ["peanuts", "shellfish"],
                "contact_details": {"phone": "123-456-7890", "emergency": "987-654-3210"}}

patient_1 = PatientData(**patient_data)

add_patient_data(patient_1)
```

## Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class PatientData(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Kishor', 'gender': 'male', 'age': 40, 'address': address1}

patient1 = PatientData(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address)
print(patient1.address.city)
```

## Serialization

```python
from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class PatientData(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Kishor', 'gender': 'male', 'age': 40, 'address': address1}

patient1 = PatientData(**patient_dict)

# temp = patient1.model_dump()
temp = patient1.model_dump_json()

print(temp)
print(type(temp))
```
