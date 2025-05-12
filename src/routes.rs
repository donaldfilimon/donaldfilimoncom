use rocket_dyn_templates::{context, Template};

#[get("/?<name>")]
pub fn index(name: Option<&str>) -> Template {
    Template::render(
        "index",
        context! {
          name: name.unwrap_or_else(|| "world")
        },
    )
}
