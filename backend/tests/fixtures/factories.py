from polyfactory.factories.pydantic_factory import ModelFactory
from app.models.flow import Flow
from polyfactory.pytest_plugin import register_fixture


@register_fixture
class FlowFactory(ModelFactory[Flow]):
    __model__ = Flow
