using Microsoft.AspNetCore.Mvc;

namespace EduFlow.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class UsersController : ControllerBase
{
    [HttpGet("ping")]
    public IActionResult Ping() => Ok(new { status = "ok", service = "EduFlow.Api" });
}
